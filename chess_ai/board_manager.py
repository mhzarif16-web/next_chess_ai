import chess

class BoardManager:
    def __init__(self):
        self.board = chess.Board()

    def show_board(self):
        print(self.board)

    def get_legal_moves(self):
        return list(self.board.legal_moves)

    def make_move(self, move):
        self.board.push(move)

    def get_fen(self):
        return self.board.fen()

    def game_over(self):
        return self.board.is_game_over()
