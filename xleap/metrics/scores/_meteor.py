from logging import getLogger

import evaluate

from ..config import config
from ..core import register_metric
from ..data_row import DataRow

_meteor_registered = False

logger = getLogger(__name__)


def init():
    global _meteor_registered

    if not config.reference_corpus:
        logger.info("No reference corpus provided for NLP scores. Skipping NLP scores.")

    if _meteor_registered:
        return

    response_column = config.response_column
    _corpus = config.reference_corpus

    meteor = evaluate.load("meteor")
    _meteor_registered = True

    @register_metric([response_column])
    def meteor_score(text: DataRow):
        return meteor.compute(
            predictions=[text.get(response_column)],
            references=[_corpus],
        )["meteor"]
