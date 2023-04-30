from typing import Self

class SheetStockType:
    def __init__(self: Self, length: float, width: float, nominalThickness: float):
        self.__length = length
        self.__width = width
        self.__nominalThickness = nominalThickness

    def GetLength(self: Self) -> float:
        return self.__length
    
    def GetWidth(self: Self) -> float:
        return self.__width
    
    def GetNominalThickness(self: Self) -> float:
        return self.__nominalThickness