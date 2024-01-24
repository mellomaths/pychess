from chess.piece import Piece
from chess.pieces.queen import Queen
from chess.types import Side


class Pawn(Piece):
    desc = "Pawn"

    def __repr__(self):
        return self.desc

    def __str__(self):
        return self.desc

    def promote(self):
        return Queen(self.side, self.position)

    def is_move_allowed(self, x: int, y: int) -> bool:
        new_position = (x, y)

        if new_position == self.position:
            return False

        is_first_move = self.spawn[0] + 2 == new_position[
            0] or self.spawn[0] - 2 == new_position[0]
        is_any_move = self.position[0] + 1 == new_position[
            0] or self.position[0] - 1 == new_position[0]

        is_moving_towards = self.position[1] == new_position[1]
        is_eating_a_piece_r = self.position[1] + 1 == new_position[1]
        is_eating_a_piece_l = self.position[1] - 1 == new_position[1]
        return (is_first_move
                or is_any_move) and (is_moving_towards or is_eating_a_piece_r
                                     or is_eating_a_piece_l)


class WhitePawn(Pawn):

    def __init__(self, i: int = 0) -> None:
        spawn = (6, i)
        super().__init__(side=Side.WHITE, spawn=spawn)


class BlackPawn(Pawn):

    def __init__(self, i: int = 0) -> None:
        spawn = (1, i)
        super().__init__(side=Side.BLACK, spawn=spawn)
