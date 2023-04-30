from pycut.algorithms import base
from pycut.types import sheetstocktype
from typing import List, Self

SheetList = List[sheetstocktype.SheetStockType]

class Guillotine(base.Base):
    def Run(self: Self, inputs: SheetList, outputs: SheetList):
        self._inputSheets = inputs
        self._outputSheets = outputs
