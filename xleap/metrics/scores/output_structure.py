import json
from dataclasses import dataclass

from langchain.prompts import HumanMessagePromptTemplate
from openai.types.chat import ChatCompletionSystemMessageParam
from pandas import Series

from xleap.metrics.common import ItemResult, LLMMetric
from xleap.metrics.config import config
from xleap.metrics.validation import EvaluationMode

OUTPUT_STRUCTURE = HumanMessagePromptTemplate.from_template(
    """
Given the following question which has all the related context available within and the response

please output a structure score on a scale of 0 to 1 on how appropriately the response is to structured as per the question requirements in the following format
distribute equal score for each specified criteria in the question.
("score": "<insert score here>", "reason": "<insert reason here in all cases>")

If not structured as per the requirements, or if you believe the answer is not readable, return the json payload
("score": null, "reason": "response is unorganized")

you're not allowed to make any changes to sentences given
you're required to output a reason for all cases

question: {question}
response: {response}
output:"""  # noqa: E501
)


@dataclass
class OutputStructure(LLMMetric):
    """
    Attributes
    ----------
    name : str
    batch_size : int
        Batch size for openai completion.
    """

    name: str = "output_structure"
    evaluation_mode: EvaluationMode = EvaluationMode.qac
    batch_size: int = 15

    def __post_init__(self):
        pass

    def init_model(self):
        pass

    def compute(self, df: Series, force=False) -> ItemResult:
        exists = super().compute(df, force)
        if exists:
            return exists

        human_prompt = OUTPUT_STRUCTURE.format(
            question=df[config.prompt_column], response=df[config.response_column]
        )

        result = self.llm._client.chat.completions.create(
            messages=[
                ChatCompletionSystemMessageParam(
                    content=human_prompt.content, role="system"
                )
            ],
            n=1,
            temperature=0,
            model=self.llm.model,
        )

        self._logger.info(
            f"{self.name} for {df.get('id')} got {result.choices[0].message.content}"
        )
        res = json.loads(result.choices[0].message.content)

        return ItemResult(value=str(res.get("score")), reason=str(res.get("reason")))
