from typing import Self

class SheetType:
    def __init__(self: Self, length: float, width: float, numberAvailable: int = 1):
        self._length = length
        self._width = width
        self._numberAvailable = numberAvailable

    def GetLength(self: Self) -> float:
        return self._length
    
    def GetWidth(self: Self) -> float:
        return self._width
    
    def GetNumberAvailable(self: Self) -> int:
        return self._numberAvailable