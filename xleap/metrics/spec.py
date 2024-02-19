import logging
from dataclasses import dataclass
from typing import Any, Callable, Dict

from xleap.metrics.data_row import DataRow

logger = logging.getLogger(__name__)


@dataclass
class UdfSpec:
    col_names: list[str]
    udfs: Dict[str, Callable[[Any], Any]]
    name: str | None = None
    prefix: str | None = None
    row_type: DataRow = DataRow

    def __post_init__(self):
        if not isinstance(self.col_names, list):
            raise ValueError(
                f"col_names should be a list of strings got {type (self.col_names)}"
            )

    def run(self, data: DataRow, schema_name: str | None = None):
        assert all(
            [data.has(col_name) for col_name in self.col_names]
        ), f"{self.col_names} values should be available on data row"

        for metric_name, metric_func in self.udfs.items():
            name = f"{schema_name}.{metric_name}" if schema_name else f"{metric_name}"

            if data.has(name):
                continue

            try:
                res = metric_func(data)
                data.set(name, res)
            except BaseException:
                logger.exception(f"Evaluating UDF {name} failed")


class ResolverSpec:
    ...


class MetricSpec:
    ...


class Metric:
    ...
