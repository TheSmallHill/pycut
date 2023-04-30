from abc import ABC, abstractmethod
from pycut.types import sheetstocktype
from typing import List, Self

SheetList = List[sheetstocktype.SheetStockType]

class Base(ABC):
    @abstractmethod
    def Run(self: Self):
        pass