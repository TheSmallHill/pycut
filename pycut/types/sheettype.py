from typing import Self

class SheetType:
    def __init__(self: Self, length: float, width: float):
        self.__length = length
        self.__width = width

    def GetLength(self: Self) -> float:
        return self.__length
    
    def GetWidth(self: Self) -> float:
        return self.__width