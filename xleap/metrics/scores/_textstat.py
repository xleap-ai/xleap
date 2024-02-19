from dataclasses import dataclass
from logging import getLogger
from typing import Callable

from ..config import config
from ..core import register_metric
from ..data_row import DataRow

_textstat_registered = False

logger = getLogger(__name__)


def wrapper(stat_name: str, column: str) -> Callable[[DataRow], list]:
    import textstat

    stat = textstat.textstat.__getattribute__(stat_name)

    def wrappee(text: DataRow) -> list:
        input = getattr(text, column)
        return stat(input)

    return wrappee


def init():
    global _textstat_registered

    if _textstat_registered:
        return

    _textstat_registered = True

    columns = [config.prompt_column, config.response_column]

    for column in columns:
        for metric in text_stat_metrics:
            register_metric(columns, udf_name=f"{column}.{metric.stat_name}")(
                wrapper(metric.stat_name, column)
            )


@dataclass
class StatMetric:
    stat_name: str
    schema_name: str = ""
    udf_name: str | None = None


text_stat_metrics: list[StatMetric] = [
    StatMetric("flesch_kincaid_grade", "text_standard_component"),
    StatMetric("flesch_reading_ease"),
    StatMetric("smog_index", "text_standard_component"),
    StatMetric("coleman_liau_index", "text_standard_component"),
    StatMetric("automated_readability_index"),
    StatMetric("dale_chall_readability_score", "text_standard_component"),
    StatMetric("linsear_write_formula", "text_standard_component"),
    StatMetric("gunning_fog", "text_standard_component"),
    StatMetric("text_standard", udf_name="aggregate_reading_level"),
    StatMetric("fernandez_huerta", "es"),
    StatMetric("szigriszt_pazos", "es"),
    StatMetric("gutierrez_polini", "es"),
    StatMetric("crawford", "es"),
    StatMetric("gulpease_index", "it"),
    StatMetric("osman", "ar"),
    # count metrics
    StatMetric("syllable_count"),
    StatMetric("lexicon_count"),
    StatMetric("sentence_count"),
    StatMetric("char_count", udf_name="character_count"),
    StatMetric("letter_count"),
    StatMetric("polysyllabcount", udf_name="polysyllable_count"),
    StatMetric("monosyllabcount", udf_name="monosyllable_count"),
    StatMetric("difficult_words"),
]
