from chess.piece import Piece
from chess.types import Side


class Knight(Piece):
    desc = "Knight"

    def __repr__(self):
        return self.desc

    def __str__(self):
        return self.desc

    def is_move_allowed(self, x: int, y: int) -> bool:
        new_position = (x, y)

        if new_position == self.position:
            return False

        # x + 1 ou x - 1 => y + 2 ou y - 2
        # y + 1 ou y - 1 => x + 2 ou x - 2
        # x + 2 ou x - 2 => y + 1 ou y - 1
        # y + 2 ou y - 2 => x + 1 ou x - 1

        current_x, current_y = self.position
        return (((current_x + 1 == x or current_x - 1 == x) and
                 (current_y + 2 == y or current_y - 2 == y))
                or ((current_y + 1 == x or current_y - 1 == x) and
                    (current_x + 2 == y or current_x - 2 == y))
                or ((current_x + 2 == x or current_x - 2 == x) and
                    (current_y + 1 == y or current_y - 1 == y))
                or ((current_y + 1 == x or current_y - 1 == x) and
                    (current_x + 2 == y or current_x - 2 == y)))


class WhiteKnight(Knight):

    def __init__(self, i: int = 0) -> None:
        spawn = (7, 1 if i == 0 else 6)
        super().__init__(side=Side.WHITE, spawn=spawn)


class BlackKnight(Knight):

    def __init__(self, i: int = 0) -> None:
        spawn = (0, 1 if i == 0 else 6)
        super().__init__(side=Side.BLACK, spawn=spawn)
