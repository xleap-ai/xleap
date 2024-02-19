from dataclasses import dataclass

from pandas import Series

from xleap.metrics.common import ItemResult, Metric
from xleap.metrics.config import config
from xleap.metrics.validation import EvaluationMode


@dataclass
class PromptSentiment(Metric):
    lexicon: str = config.sentiment_lexicon
    name = "prompt.sentiment_nltk"
    evaluation_mode = EvaluationMode.q

    column: str = config.prompt_column

    _nltk_downloaded = False

    def init_model(self):
        import nltk
        from nltk.sentiment import SentimentIntensityAnalyzer

        if not self._nltk_downloaded:
            nltk.download(self.lexicon)
            self._nltk_downloaded = True

        self._stat = SentimentIntensityAnalyzer()

    def compute(self, df: Series, force=False) -> ItemResult:
        return super().compute(df, force) or ItemResult(
            value=self._stat.polarity_scores(df[self.column])["compound"]
        )


class ResponseSentiment(PromptSentiment):
    name = "response.sentiment_nltk"
    evaluation_mode = EvaluationMode.a
    column: str = config.response_column
