from dataclasses import dataclass
from logging import getLogger

import pandas as pd
import textstat

from xleap.metrics.common import ItemResult, Metric
from xleap.metrics.config import config
from xleap.metrics.validation import EvaluationMode

logger = getLogger(__name__)


@dataclass
class TextStatMetric(Metric):
    column: str
    stat_metric: "TextStatLabel"

    @property
    def evaluation_mode(self) -> str:
        if self.column == config.prompt_column:
            return EvaluationMode.q
        if self.column == config.response_column:
            return EvaluationMode.a

    @property
    def name(self) -> str:
        return f"{self.column}.{self.stat_metric.stat_name}"

    def init_model(self):
        self._stat = textstat.textstat.__getattribute__(self.stat_metric.stat_name)

    def compute(self, df: pd.Series, force=False) -> ItemResult:
        return super().compute(df, force) or ItemResult(
            value=self._stat(df[self.column]), reason=None
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} ({self.name})"


@dataclass
class TextStatLabel:
    stat_name: str
    schema_name: str = ""
    udf_name: str | None = None


_text_stat_metrics: list[TextStatLabel] = [
    TextStatLabel("flesch_kincaid_grade", "text_standard_component"),
    TextStatLabel("flesch_reading_ease"),
    TextStatLabel("smog_index", "text_standard_component"),
    TextStatLabel("coleman_liau_index", "text_standard_component"),
    TextStatLabel("automated_readability_index"),
    TextStatLabel("dale_chall_readability_score", "text_standard_component"),
    TextStatLabel("linsear_write_formula", "text_standard_component"),
    TextStatLabel("gunning_fog", "text_standard_component"),
    TextStatLabel("text_standard", udf_name="aggregate_reading_level"),
    TextStatLabel("fernandez_huerta", "es"),
    TextStatLabel("szigriszt_pazos", "es"),
    TextStatLabel("gutierrez_polini", "es"),
    TextStatLabel("crawford", "es"),
    TextStatLabel("gulpease_index", "it"),
    TextStatLabel("osman", "ar"),
    # count metrics
    TextStatLabel("syllable_count"),
    TextStatLabel("lexicon_count"),
    TextStatLabel("sentence_count"),
    TextStatLabel("char_count", udf_name="character_count"),
    TextStatLabel("letter_count"),
    TextStatLabel("polysyllabcount", udf_name="polysyllable_count"),
    TextStatLabel("monosyllabcount", udf_name="monosyllable_count"),
    TextStatLabel("difficult_words"),
]

text_stat_metrics: list[Metric] = []
columns = [config.prompt_column, config.response_column]

for column in columns:
    for metric in _text_stat_metrics:
        ins = TextStatMetric(
            batch_size=config.batch_size, stat_metric=metric, column=column
        )
        text_stat_metrics.append(ins)
