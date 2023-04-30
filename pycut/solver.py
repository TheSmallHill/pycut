from pycut.types import sheettype
from typing import Self

SheetType = sheettype.SheetType

class Solver:
    __stockSheetsSize = None
    __numStockSheets = 0

    __cutPieces = []
    __algo = None # @TODO fill this in with some default

    def AddStockSheets(self: Self, sheet: SheetType, numSheets: int) -> None:        
        self.__stockSheetsSize = sheet
        self.__numStockSheets = numSheets

    def ClearStockSheets(self: Self) -> None:
        self.AddStockSheets(None, 0)

    def AddCutPieces(self: Self, piece: SheetType | list) -> None:
        shouldRaise = False
        if isinstance(piece, sheettype.SheetStockType):
            self.__cutPieces.append(piece)
        elif isinstance(piece, list):
            if all(isinstance(x, sheettype.SheetStockType) for x in piece):
                self.__cutPieces.extend(piece)
            else:
                shouldRaise = True
        else:
            shouldRaise = True

        if shouldRaise:
            raise TypeError("Input/Output data must be provided as pycut.types.sheetstocktype.SheetStockType type")
        
    def ClearCutPieces(self: Self) -> None:
        self.__cutPieces.clear()