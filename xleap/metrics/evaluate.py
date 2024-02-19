import logging

import pandas as pd

from xleap.metrics.common import Metric

logger = logging.getLogger(__name__)


def evaluate(
    dataset: pd.DataFrame,
    metrics: list[Metric] | None = None,
    column_map: dict[str, str] = {},
    force=False,
) -> pd.DataFrame:
    """
    Run the evaluation on the dataset with different metrics

    Parameters
    ----------
    dataset : pd.DataFrame
    column_map : dict[str, str], optional
    """

    if dataset is None:
        raise ValueError("Provide dataset!")

    if metrics is None:
        raise ValueError("Provide metrics to evaluate!")

    metrics_names = [m.name for m in metrics]

    if len(set(metrics_names)) != len(metrics_names):
        logger.warn("metrics are repeating!")

    # remap column names from the dataset
    if column_map:
        dataset.rename(columns=column_map, inplace=True)

    # run the evaluation on dataset with different metrics
    # initialize all the models in the metrics

    [m.init_model() for m in metrics]

    for metric in metrics:
        logger.info(f"evaluating with [{metric.name}]")

        # _force = metric.name not in dataset.columns
        # dataset: pd.Series = dataset.apply(lambda x: metric.compute(x, force=force or _force), axis=1)

        dataset.loc[:, metric.name] = metric.score(dataset, force=force)

    return dataset
