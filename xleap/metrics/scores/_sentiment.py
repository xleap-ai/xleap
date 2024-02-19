from typing import Optional

from ..config import XleapMetricConfig, config
from ..core import register_metric
from ..data_row import DataRow

_prompt = config.prompt_column
_response = config.response_column
_sentiment_analyzer = None
_nltk_downloaded = False


def sentiment_nltk(text: str) -> float:
    if _sentiment_analyzer is None:
        raise ValueError(
            "sentiment metrics must initialize sentiment analyzer before evaluation!"
        )
    return _sentiment_analyzer.polarity_scores(text)["compound"]


@register_metric([_prompt], udf_name=f"{_prompt}.sentiment_nltk")
def prompt_sentiment(text: DataRow):
    return sentiment_nltk(text.get(_prompt))


@register_metric([_response], udf_name=f"{_response}.sentiment_nltk")
def response_sentiment(text: DataRow):
    return sentiment_nltk(text.get(_response))


def init(lexicon: Optional[str] = None, config: Optional[XleapMetricConfig] = config):
    import nltk
    from nltk.sentiment import SentimentIntensityAnalyzer

    lexicon = lexicon or config.sentiment_lexicon
    global _sentiment_analyzer, _nltk_downloaded

    if not _nltk_downloaded:
        nltk.download(lexicon)
        _nltk_downloaded = True

    _sentiment_analyzer = SentimentIntensityAnalyzer()
