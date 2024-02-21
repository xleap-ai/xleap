import json
from dataclasses import dataclass

from langchain.prompts import HumanMessagePromptTemplate
from openai.types.chat import ChatCompletionSystemMessageParam
from pandas import Series

from xleap.metrics.common import ItemResult, LLMMetric
from xleap.metrics.config import config
from xleap.metrics.validation import EvaluationMode

CONTEXT_RELEVANCE = HumanMessagePromptTemplate.from_template(
    """
Given the following question which has all the related context available within,

please output a relevancy score on a scale of 0 to 1 on how relevant the context is to answer the question in the following format
("score": "", "reason": "")

If no relevant sentences are found, or if you believe the question cannot be answered from the given context, return the json payload
("score": null, "reason": "Insufficient Information")

While extracting candidate sentences you're not allowed to make any changes to sentences given.
you're required to output a reason for all cases

question: {question}
output:"""  # noqa: E501
)


@dataclass
class ContextRelevancy(LLMMetric):
    """
    Attributes
    ----------
    name : str
    batch_size : int
        Batch size for openai completion.
    """

    name: str = "context_relevancy"
    evaluation_mode: EvaluationMode = EvaluationMode.q
    batch_size: int = 15

    def __post_init__(self):
        pass

    def init_model(self):
        pass

    def compute(self, df: Series, force=False) -> ItemResult:
        exists = super().compute(df, force)
        if exists:
            return exists

        q = df[config.prompt_column]

        human_prompt = CONTEXT_RELEVANCE.format(question=q)
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
