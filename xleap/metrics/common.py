import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from math import floor

import pandas as pd
from tqdm import tqdm

from xleap.metrics.llm_factory import XLeapLLM, llm_factory
from xleap.metrics.validation import EvaluationMode


@dataclass
class ItemResult:
    value: str
    reason: str | None = None

    def __bool__(self):
        return bool(self.value)


def make_batches(total_size: int, batch_size: int) -> list[range]:
    """
    Take a total size and batch size and return a list of ranges for the batches
    """
    tail = total_size % batch_size
    num_batches = floor(total_size / batch_size)
    batches = [
        range(i, i + batch_size) for i in range(0, batch_size * num_batches, batch_size)
    ]
    if tail != 0:
        batches.append(range(batch_size * num_batches, batch_size * num_batches + tail))

    return batches


@dataclass
class Metric(ABC):
    batch_size: int
    _logger = logging.getLogger(__name__)

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @property
    @abstractmethod
    def evaluation_mode(self) -> EvaluationMode:
        ...

    @abstractmethod
    def init_model(self):
        """
        This method will lazy initialize the model.
        """
        ...

    def score(self, dataset: pd.DataFrame, force=False) -> list[ItemResult]:
        scores: list[ItemResult] = []
        _force = self.name not in dataset.columns

        for batch in tqdm(self.get_batches(len(dataset)), desc=self.name):
            score = self._score_batch(dataset.loc[batch], force=_force or force)
            scores.extend(score)

        return scores

    def _score_batch(self, dataset: pd.DataFrame, force=False) -> list[ItemResult]:
        results = []
        for i, j in dataset.iterrows():
            try:
                results.append(self.compute(j, force=force))
            except:
                results.append(ItemResult(value=None))

        return results

    @abstractmethod
    def compute(self, df: pd.Series, force=False) -> ItemResult:
        f"""
        compute {self.name} metric for each row of dataset
        by default metric will not be evaluated if it has already been evaluated.

        set force=True to re-evaluate metric all the times
        """
        if not force and df[self.name] is not None:
            self._logger.debug(
                f"skipping metric {self.name}: already evaluated for {df.get('id')}"
            )
            return df[self.name]

    def get_batches(self, dataset_size: int) -> list[range]:
        return make_batches(dataset_size, self.batch_size)


@dataclass
class LLMMetric(Metric):
    llm: XLeapLLM = field(default_factory=llm_factory)
