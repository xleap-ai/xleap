import logging

import evaluate

from ..config import config
from ..core import register_metric
from ..data_row import DataRow

_bleu_registered = False

logger = logging.getLogger(__name__)


def init():
    global _bleu_registered

    if not config.reference_corpus:
        logger.info("No reference corpus provided for NLP scores. Skipping NLP scores.")

    if _bleu_registered:
        return

    response_column = config.response_column
    _corpus = config.reference_corpus

    bleu = evaluate.load("bleu")
    _bleu_registered = True

    @register_metric([response_column])
    def bleu_score(text: DataRow):
        return bleu.compute(
            predictions=[text.get(response_column)],
            references=[_corpus],
        )["bleu"]
