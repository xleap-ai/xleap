from pandas import Series

from xleap.metrics.common import ItemResult, Metric
from xleap.metrics.config import config
from xleap.metrics.validation import EvaluationMode


class BLEU(Metric):
    name = "bleu"
    evaluation_mode = EvaluationMode.a

    def init_model(self):
        import evaluate

        self._stat = evaluate.load("bleu")

    def compute(self, df: Series, force=False) -> ItemResult:
        return super().compute(df, force) or ItemResult(
            value=self._stat.compute(
                predictions=[df[config.response_column]],
                references=[config.reference_corpus],
            )["bleu"]
        )


class Rouge(Metric):
    name = "rouge"
    evaluation_mode = EvaluationMode.a

    def init_model(self):
        import evaluate

        self._stat = evaluate.load("rouge")

    def compute(self, df: Series, force=False) -> ItemResult:
        return super().compute(df, force) or ItemResult(
            value=self._stat.compute(
                predictions=[df[config.response_column]],
                references=[config.reference_corpus],
                rouge_types=[config.rouge_type],
            )[config.rouge_type]
        )


class Meteor(Metric):
    name = "meteor"
    evaluation_mode = EvaluationMode.a

    def init_model(self):
        import evaluate

        self._stat = evaluate.load("meteor")

    def compute(self, df: Series, force=False) -> ItemResult:
        return super().compute(df, force) or ItemResult(
            value=self._stat.compute(
                predictions=[df[config.response_column]],
                references=[config.reference_corpus],
            )["meteor"]
        )
