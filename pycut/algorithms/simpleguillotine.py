from pycut.algorithms import base
from pycut.types import sheetstocktype
from typing import List, Self

SheetList = List[sheetstocktype.SheetStockType]

class SimpleGuillotine(base.Base):
    """Simple guillotine cutting algorithm based on the paper found at https://link.springer.com/article/10.1186/2251-712X-8-21."""

    def Run(self: Self, inputs: SheetList, outputs: SheetList):
        self._inputSheets = inputs
        self._outputSheets = outputs
