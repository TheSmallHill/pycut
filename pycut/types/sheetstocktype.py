from typing import Self

class SheetStockType:
    def __init__(self: Self, length: float, width: float, nominalThickness: float):
        self._length = length
        self._width = width
        self._nominalThickness = nominalThickness