from pycut.algorithms import base
from pycut.types import sheettype
from typing import List, Self

class AugmentedSheetType(sheettype.SheetType):
    def __init__(self: Self, sheet: sheettype.SheetType):
        # Basically a deep copy constructor for what already exists...
        super().__init__(sheet._length, sheet._width)

        # ... and then doing some extra calculations for the guillotine algorithm
        self._area = self._CalculateArea(self._length, self._width)
        self._demand = self._CalculateDemand(self._area, self._numberAvailable)

    def _CalculateArea(self: Self, length: float, width: float) -> float:
        return length * width
    
    def _CalculateDemand(self: Self, area: float, quantity: int) -> float:
        return area * quantity

SheetList = List[sheettype.SheetStockType]
AugmentedSheetList = List[AugmentedSheetType]

class SimpleGuillotine(base.Base):
    """Simple guillotine cutting algorithm based on the paper found at https://link.springer.com/article/10.1186/2251-712X-8-21."""

    def Run(self: Self, inputs: SheetList, outputs: SheetList):
        self._inputSheets = inputs
        self._outputSheets = self._UpgradeSheetsToAugmentedSheets(outputs)

        self._totalDemand = self._CalculateTotalDemand(self._outputSheets)

    def _CalculateTotalDemand(self: Self, sheets: SheetList) -> float:
        return sum(sheet.demand for sheet in sheets)
    
    def _UpgradeSheetsToAugmentedSheets(self: Self, sheets: SheetList) -> AugmentedSheetList:
        return [AugmentedSheetType(sheet) for sheet in sheets]
