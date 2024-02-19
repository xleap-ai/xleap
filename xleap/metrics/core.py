import logging
from collections import defaultdict
from copy import deepcopy
from typing import Any, Callable, Dict, List, Optional

from .data_row import DataRow
from .spec import Metric, MetricSpec, ResolverSpec, UdfSpec

logger = logging.getLogger(__name__)

_multicolumn_udfs: Dict[str, List[UdfSpec]] = defaultdict(list)
_resolver_specs: Dict[str, List[ResolverSpec]] = defaultdict(list)


def register_metric(
    col_names: List[str],
    udf_name: Optional[str] = None,
    metrics: Optional[List[MetricSpec]] = None,
    namespace: Optional[str] = None,
    schema_name: str = "",
    anti_metrics: Optional[List[Metric]] = None,
) -> Callable[[Any], Any]:
    """
    Decorator to easily configure UDFs for your data set. Decorate your UDF
    functions, then call generate_udf_dataset_schema() to create a UdfSchema
    that includes the UDFs configured by your decorator parameters.


    Specify udf_name to give the output of the UDF a name.
    udf_name
    defaults to the name of the decorated function.
    Note that all lambdas are
    named "lambda", so omitting udf_name on more than one lambda will result
    in name collisions.

    namespace:
    If you pass a namespace, it will be prepended to the UDF name.

    schema_name:
    Specifying schema_name will register the UDF in a particular schema.
    If omitted, it will be registered to the default schema.

    If any metrics are passed via the metrics argument, they will be attached
    to the column produced by the UDF via the schema returned by generate_udf_dataset_schema().

    If metrics is None, the UDF output column will get the metrics determined by
    the other resolvers passed to generate_udf_dataset_schema(), or the STANDARD_UDF_RESOLVER
    by default.
    Any anti_metrics will be excluded from the metrics attached to the UDF output.
    """

    def decorator_register(func):
        global _multicolumn_udfs, _resolver_specs
        name = udf_name or func.__name__
        name = f"{namespace}.{name}" if namespace else name
        _multicolumn_udfs[schema_name].append(UdfSpec(col_names, {name: func}))

        if metrics:
            _resolver_specs[schema_name].append(
                ResolverSpec(name, None, deepcopy(metrics))
            )
        if anti_metrics:
            _resolver_specs[schema_name].append(
                ResolverSpec(name, None, [MetricSpec(m) for m in anti_metrics], True)
            )

        return func

    return decorator_register


def unregister_udf(
    udf_name: str, namespace: Optional[str] = None, schema_name: str = ""
) -> None:
    global _multicolumn_udfs, _resolver_specs
    name = f"{namespace}.{udf_name}" if namespace else udf_name
    if schema_name not in _multicolumn_udfs:
        logger.warn(
            f"Can't unregister UDF {name} from non-existant schema {schema_name}"
        )
        return

    found = False
    for spec in _multicolumn_udfs[schema_name]:
        if name in spec.udfs:
            found = True
            del spec.udfs[name]
    if not found:
        logger.warn(f"UDF {name} could not be found for unregistering")
    _resolver_specs[schema_name] = list(
        filter(lambda x: x.column_name != name, _resolver_specs[schema_name])
    )


def _run_udfs_on_row(data: DataRow):
    for schema_name, udf_specs in _multicolumn_udfs.items():
        for spec in udf_specs:
            spec.run(data, schema_name=schema_name)
