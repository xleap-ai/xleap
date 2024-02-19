import logging
from typing import Callable, Optional

from sentence_transformers import util

from xleap.metrics.data_row import DataRow

from ..config import XleapMetricConfig, config
from ..core import register_metric
from ..transformer import Encoder

_prompt = config.prompt_column
_response = config.response_column
_transformer_model = None

logger = logging.getLogger(__name__)


def init(
    transformer_name: Optional[str] = None,
    custom_encoder: Optional[Callable] = None,
    config: Optional[XleapMetricConfig] = config,
):
    global _transformer_model
    if transformer_name is None and custom_encoder is None:
        transformer_name = config.transformer_name
    _transformer_model = Encoder(transformer_name, custom_encoder)


@register_metric([_prompt, _response], f"{_response}.relevance_to_{_prompt}")
def prompt_response_similarity(data: DataRow):
    global _transformer_model

    if _transformer_model is None:
        raise ValueError(
            "response.relevance_to_prompt must have a transformer model initialized before use."
        )

    x, y = data.get("prompt"), data.get("response")

    try:
        embedding_1 = _transformer_model.encode([x] if isinstance(x, str) else x)
        embedding_2 = _transformer_model.encode([y] if isinstance(y, str) else y)
        similarity = util.pytorch_cos_sim(embedding_1, embedding_2)
        return similarity.item()
    except Exception as e:
        logger.warning(
            f"prompt_response_similarity encountered error {e} for text: {data}"
        )
