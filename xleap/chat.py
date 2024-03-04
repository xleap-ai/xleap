import json
import logging
import os
from dataclasses import dataclass, field
from uuid import uuid4

from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam

logger = logging.getLogger(__name__)


@dataclass
class ChatInterface:
    model: str
    system_prompt: str = "you are a helpful assistant"

    id: str = field(default_factory=lambda: uuid4().hex)
    api_key: str | None = None
    base_url: str | None = None

    messages: list[ChatCompletionMessageParam] = field(default_factory=list)

    def __post_init__(self):
        self.ai = OpenAI(api_key=self.api_key, base_url=self.base_url)
        self.messages = [
            {"role": "system", "content": self.system_prompt}
        ] + self.messages

    def append(self, message: ChatCompletionMessageParam):
        self.messages.append(message)
        return self.chat_with_ai()

    def chat_with_ai(self):
        res = self.ai.chat.completions.create(
            messages=(self.messages[0:1] + self.messages[-2:])
            if len(self.messages) > 4
            else self.messages,
            model=self.model,
            temperature=0,
            response_format={
                "type": "json_object",
                # "schema": {
                #     "type": "object",
                #     "properties": {"intent": {"type": "string"}, "arguments": {"type": "string"}},
                #     "required": ["intent", "arguments"],
                # },
            },
        )
        logger.debug(res.model_dump_json())

        message = res.choices[0].message
        self.messages.append({"role": message.role, "content": message.content})

        return res

    def dump(self):
        print(self.messages, self.id)
        filename = f"conversations/{self.model}-{self.id}.json"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as d:
            d.write(json.dumps(self.messages, indent=2))
