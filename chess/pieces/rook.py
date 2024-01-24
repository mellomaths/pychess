from chess.piece import Piece
from chess.types import Side


class Rook(Piece):
    desc = "Rook"

    def __repr__(self):
        return self.desc

    def __str__(self):
        return self.desc


class WhiteRook(Rook):

    def __init__(self, i: int = 0) -> None:
        spawn = (7, 0 if i == 0 else 7)
        super().__init__(side=Side.WHITE, spawn=spawn)


class BlackRook(Rook):

    def __init__(self, i: int = 0) -> None:
        spawn = (0, 0 if i == 0 else 7)
        super().__init__(side=Side.BLACK, spawn=spawn)
