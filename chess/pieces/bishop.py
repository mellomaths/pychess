from chess.piece import Piece
from chess.types import Side


class Bishop(Piece):
    desc = "Bishop"

    def __repr__(self):
        return self.desc

    def __str__(self):
        return self.desc

    def is_move_allowed(self, x: int, y: int) -> bool:
        new_position = (x, y)

        if new_position == self.position:
            return False

        diff_x = x - self.position[0]
        diff_y = y - self.position[1]
        is_diagonal = abs(diff_x) == abs(diff_y)
        return is_diagonal


class WhiteBishop(Bishop):

    def __init__(self, i: int = 0) -> None:
        spawn = (7, 2 if i == 0 else 5)
        super().__init__(Side.WHITE, spawn)


class BlackBishop(Bishop):

    def __init__(self, i: int = 0) -> None:
        spawn = (0, 2 if i == 0 else 5)
        super().__init__(Side.BLACK, spawn)
