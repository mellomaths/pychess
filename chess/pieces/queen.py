from chess.piece import Piece
from chess.types import Side


class Queen(Piece):
    desc = "Queen"

    def __repr__(self):
        return self.desc

    def __str__(self):
        return self.desc


class WhiteQueen(Queen):

    def __init__(self) -> None:
        spawn = (7, 3)
        super().__init__(side=Side.WHITE, spawn=spawn)


class BlackQueen(Queen):

    def __init__(self) -> None:
        spawn = (0, 3)
        super().__init__(side=Side.BLACK, spawn=spawn)
