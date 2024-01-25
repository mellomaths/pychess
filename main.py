from chess.game import Chess

if __name__ == "__main__":
    chess = Chess()

    chess.show_board()
    pawn = chess.board.get_piece_in_place(6, 3)
    chess.board.move_piece(piece=pawn, x=4, y=3)
    chess.show_board()

    pawn = chess.board.get_piece_in_place(1, 4)
    chess.board.move_piece(piece=pawn, x=3, y=4)
    chess.show_board()

    pawn = chess.board.get_piece_in_place(4, 3)
    chess.board.move_piece(piece=pawn, x=3, y=4)
    chess.show_board()

    knight = chess.board.get_piece_in_place(0, 1)
    chess.board.move_piece(piece=knight, x=2, y=2)
    chess.show_board()

    knight = chess.board.get_piece_in_place(7, 6)
    chess.board.move_piece(piece=knight, x=5, y=5)
    chess.show_board()

    knight = chess.board.get_piece_in_place(2, 2)
    chess.board.move_piece(piece=knight, x=3, y=4)
    chess.show_board()

    bishop = chess.board.get_piece_in_place(7, 2)
    chess.board.move_piece(piece=bishop, x=3, y=6)
    chess.show_board()

    queen = chess.board.get_piece_in_place(0, 3)
    chess.board.move_piece(piece=queen, x=3, y=6)
    chess.show_board()
