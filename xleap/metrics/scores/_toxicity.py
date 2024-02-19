import os
from typing import Optional

import torch

from ..config import XleapMetricConfig, config
from ..core import register_metric
from ..data_row import DataRow

_USE_CUDA = torch.cuda.is_available() and not bool(os.getenv("XLEAP_NO_CUDA", False))


_device = 0 if _USE_CUDA else -1

_toxicity_tokenizer = None
_toxicity_pipeline = None


def toxicity(text: str) -> float:
    if _toxicity_pipeline is None or _toxicity_tokenizer is None:
        raise ValueError("toxicity score must initialize the pipeline first")

    result = _toxicity_pipeline(
        text, truncation=True, max_length=_toxicity_tokenizer.model_max_length
    )
    return (
        result[0]["score"] if result[0]["label"] == "toxic" else 1 - result[0]["score"]
    )


@register_metric(["prompt"], "prompt.toxicity")
def prompt_toxicity(text: DataRow):
    return toxicity(text.prompt)


@register_metric(["response"], "response.toxicity")
def response_toxicity(text: DataRow):
    return toxicity(text.response)


def init(
    model_path: Optional[str] = None, config: Optional[XleapMetricConfig] = config
):
    from transformers import (
        AutoModelForSequenceClassification,
        AutoTokenizer,
        TextClassificationPipeline,
    )

    model_path = model_path or config.toxicity_model_path
    global _toxicity_tokenizer, _toxicity_pipeline

    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    _toxicity_tokenizer = AutoTokenizer.from_pretrained(model_path)
    _toxicity_pipeline = TextClassificationPipeline(
        model=model, tokenizer=_toxicity_tokenizer, device=_device
    )
