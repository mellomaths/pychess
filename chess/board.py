from typing import List, Optional

from chess.piece import Piece
from chess.pieces.bishop import BlackBishop, WhiteBishop
from chess.pieces.king import BlackKing, WhiteKing
from chess.pieces.knight import BlackKnight, WhiteKnight
from chess.pieces.pawn import BlackPawn, Pawn, WhitePawn
from chess.pieces.queen import BlackQueen, WhiteQueen
from chess.pieces.rook import BlackRook, WhiteRook


class Board():
    moves: List[str] = []
    board: List[List[Optional[Piece]]] = [
        [
            BlackRook(i=0),
            BlackKnight(i=0),
            BlackBishop(i=0),
            BlackQueen(),
            BlackKing(),
            BlackBishop(i=1),
            BlackKnight(i=1),
            BlackRook(i=1)
        ],
        [
            BlackPawn(i=0),
            BlackPawn(i=1),
            BlackPawn(i=2),
            BlackPawn(i=3),
            BlackPawn(i=4),
            BlackPawn(i=5),
            BlackPawn(i=6),
            BlackPawn(i=7)
        ],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [
            WhitePawn(i=0),
            WhitePawn(i=1),
            WhitePawn(i=2),
            WhitePawn(i=3),
            WhitePawn(i=4),
            WhitePawn(i=5),
            WhitePawn(i=6),
            WhitePawn(i=7)
        ],
        [
            WhiteRook(i=0),
            WhiteKnight(i=0),
            WhiteBishop(i=0),
            WhiteQueen(),
            WhiteKing(),
            WhiteBishop(i=1),
            WhiteKnight(i=1),
            WhiteRook(i=1)
        ],
    ]

    def format_board(self):
        s = [[str(e) for e in row] for row in self.board]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        return '\n'.join(table)

    def __repr__(self):
        return self.format_board()

    def __str__(self):
        return self.format_board()

    def get_piece_in_place(self, x, y) -> Piece:
        return self.board[x][y]

    def is_move_allowed(self, piece: Piece, x: int, y: int) -> bool:
        if not piece.is_move_allowed(x, y):
            return False

        piece_in_place = self.get_piece_in_place(x, y)
        # if piece_in_place is not None:
        #     # To implement "take" action
        #     return False

        return True

    def move_piece(self, piece: Piece, x: int, y: int) -> bool:
        print(f"Moving {piece} {piece.position} to {(x, y)}")
        if not self.is_move_allowed(piece, x, y):
            print("Move not allowed")
            return False

        self.board[piece.position[0]][piece.position[1]] = None
        piece.set_position(x, y)
        self.board[x][y] = piece

        if isinstance(piece, Pawn) and (x == 0 or x == 7):
            self.board[x][y] = piece.promote()

        return True
