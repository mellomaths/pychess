from chess.piece import Piece
from chess.types import Side


class Rook(Piece):
    desc = "Rook"

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
        
        is_vertical = abs(diff_x) > 0 and diff_y == 0
        is_horizontal = abs(diff_y) > 0 and diff_x == 0
        return is_vertical or is_horizontal


class WhiteRook(Rook):

    def __init__(self, i: int = 0) -> None:
        spawn = (7, 0 if i == 0 else 7)
        super().__init__(side=Side.WHITE, spawn=spawn)


class BlackRook(Rook):

    def __init__(self, i: int = 0) -> None:
        spawn = (0, 0 if i == 0 else 7)
        super().__init__(side=Side.BLACK, spawn=spawn)
