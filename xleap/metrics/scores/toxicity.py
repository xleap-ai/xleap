import os
from dataclasses import dataclass

import torch
from pandas import Series

from xleap.metrics.common import ItemResult, Metric
from xleap.metrics.config import config
from xleap.metrics.validation import EvaluationMode

_USE_CUDA = torch.cuda.is_available() and not bool(os.getenv("XLEAP_NO_CUDA", False))


_device = 0 if _USE_CUDA else -1


@dataclass
class PromptToxicity(Metric):
    model_path: str = config.toxicity_model_path
    name = "prompt.toxicity"
    evaluation_mode = EvaluationMode.q

    def init_model(self):
        from transformers import (
            AutoModelForSequenceClassification,
            AutoTokenizer,
            TextClassificationPipeline,
        )

        model = AutoModelForSequenceClassification.from_pretrained(self.model_path)
        self._toxicity_tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        self._toxicity_pipeline = TextClassificationPipeline(
            model=model, tokenizer=self._toxicity_tokenizer, device=_device
        )

    def toxicity(self, text: str) -> float:
        if self._toxicity_pipeline is None or self._toxicity_tokenizer is None:
            raise ValueError("toxicity score must initialize the pipeline first")

        result = self._toxicity_pipeline(
            text, truncation=True, max_length=self._toxicity_tokenizer.model_max_length
        )
        return (
            result[0]["score"]
            if result[0]["label"] == "toxic"
            else 1 - result[0]["score"]
        )

    def compute(self, df: Series, force=False) -> ItemResult:
        return super().compute(df, force) or ItemResult(
            value=self.toxicity(df[config.prompt_column])
        )


class ResponseToxicity(PromptToxicity):
    name = "response.toxicity"
    evaluation_mode = EvaluationMode.a

    def compute(self, df: Series, force=False) -> ItemResult:
        return super().compute(df, force) or ItemResult(
            value=self.toxicity(df[config.response_column])
        )
