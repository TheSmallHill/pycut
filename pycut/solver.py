import types.sheetstocktype
from typing import Self

CutPieceType = types.sheetstocktype.SheetStockType
SheetStockType = types.sheetstocktype.SheetStockType

class Solver:
    __stockSheets = []
    __cutPieces = []

    def AddStockSheets(self: Self, sheet: SheetStockType | list) -> None:        
        self.__AddToIoList("__stockSheets", sheet)

    def ClearStockSheets(self: Self) -> None:
        self.__stockSheets.clear()

    def AddCutPieces(self: Self, piece: CutPieceType | list) -> None:
        self.__AddToIoList("__cutPieces", piece)
        
    def ClearCutPieces(self: Self) -> None:
        self.__cutPieces.clear()

    def __AddToIoList(self: Self, ioListName: str, values: types.sheetstocktype.SheetStockType | list) -> None:
        if not isinstance(ioListName, str):
            raise TypeError("ioListName must be a string")
        
        ioList = getattr(self, ioListName)

        shouldRaise = False
        if isinstance(values, types.sheetstocktype.SheetStockType):
            ioList.append(values)
        elif isinstance(values, list):
            if all(isinstance(x, types.sheetstocktype.SheetStockType) for x in values):
                ioList.extend(values)
            else:
                shouldRaise = True
        else:
            shouldRaise = True

        if shouldRaise:
            raise TypeError("Input/Output data must be provided as types.sheetstocktype.SheetStockType type")