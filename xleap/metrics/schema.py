import logging
from typing import Any, Callable, Collection, Dict, List, Mapping, Optional, Union

logger = logging.getLogger(__name__)


def _apply_udfs_on_row(
    values: Union[List, Dict[str, List]],
    udfs: Dict,
    new_columns: Dict[str, Any],
    input_cols: Collection[str],
) -> None:
    """multiple input columns, single output column"""
    for new_col, udf in udfs.items():
        if new_col in input_cols:
            continue

        try:
            new_columns[new_col] = udf(values)[0]
        except Exception:  # noqa
            new_columns[new_col] = None
            logger.exception(f"Evaluating UDF {new_col} failed")


def _apply_udf_on_row(
    name: str,
    prefix: Optional[str],
    values: Union[List, Dict[str, List]],
    udf: Callable,
    new_columns: Dict[str, Any],
    input_cols: Collection[str],
) -> None:
    """
    multiple input columns, multiple output columns
    udf(Union[Dict[str, List], pd.DataFrame]) -> Union[Dict[str, List], pd.DataFrame]
    """

    try:
        # TODO: Document assumption: dictionary in -> dictionary out
        for new_col, value in udf(values).items():
            new_col = prefix + "." + new_col if prefix else new_col
            new_columns[new_col] = value[0]

    except Exception as e:  # noqa
        logger.exception(f"Evaluating UDF {name} failed with error {e}")


class UdfSchema:
    def _run_udfs_on_row(
        self,
        row: Mapping[str, Any],
        new_columns: Dict[str, Any],
        input_cols: Collection[str],
    ) -> None:
        for spec in self.multicolumn_udfs:
            if spec.column_names and set(spec.column_names).issubset(set(row.keys())):
                inputs = {col: [row[col]] for col in spec.column_names}
                if spec.udf is not None:
                    _apply_udf_on_row(spec.name, spec.prefix, inputs, spec.udf, new_columns, input_cols)  # type: ignore
                else:
                    _apply_udfs_on_row(inputs, spec.udfs, new_columns, input_cols)

        for column, value in row.items():
            why_type = type(self.type_mapper(type(value)))
            for spec in self.type_udfs[why_type]:
                udfs = {f"{column}.{key}": spec.udfs[key] for key in spec.udfs.keys()}
                _apply_udfs_on_row([value], udfs, new_columns, input_cols)
