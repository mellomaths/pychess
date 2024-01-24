from chess.types import Side


class Piece():
    side: Side = Side.UNSET
    position = (-1, -1)
    spawn = (-1, -1)
    desc = ""

    def __init__(self, side=Side.UNSET, spawn=(-1, -1)) -> None:
        self.side = side
        self.position = spawn
        self.spawn = spawn

    def set_position(self, x, y):
        self.position = (x, y)

    def is_move_allowed(self, x, y):
        raise NotImplementedError()
