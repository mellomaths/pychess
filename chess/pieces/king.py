from chess.piece import Piece
from chess.types import Side


class King(Piece):
    desc = "King"

    def __repr__(self):
        return self.desc

    def __str__(self):
        return self.desc


class WhiteKing(King):

    def __init__(self) -> None:
        spawn = (7, 4)
        super().__init__(side=Side.WHITE, spawn=spawn)


class BlackKing(King):

    def __init__(self) -> None:
        spawn = (0, 4)
        super().__init__(side=Side.BLACK, spawn=spawn)
