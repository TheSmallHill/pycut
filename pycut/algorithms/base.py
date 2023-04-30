from abc import ABC, abstractmethod
from pycut.types import sheettype
from typing import List, Self

SheetList = List[sheettype.SheetStockType]

class Base(ABC):
    @abstractmethod
    def Run(self: Self, inputs: SheetList, outputs: SheetList):
        pass