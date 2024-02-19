import logging

import evaluate

from ..config import config
from ..core import register_metric
from ..data_row import DataRow

_rouge_registered = False

logger = logging.getLogger(__name__)


def init():
    global _rouge_registered

    if not config.reference_corpus:
        logger.info("No reference corpus provided for NLP scores. Skipping NLP scores.")

    if _rouge_registered:
        return

    response_column = config.response_column
    _corpus = config.reference_corpus

    rouge = evaluate.load("rouge")
    _rouge_registered = True

    _rouge_type: str = config.rouge_type

    @register_metric([response_column])
    def rouge_score(row: DataRow):
        return rouge.compute(
            predictions=[row.get(response_column)],
            references=[_corpus],
            rouge_types=[_rouge_type],
        )[_rouge_type]
