import os
import openai
from chess_ai.board_manager import BoardManager
from chess_ai.move_evaluator import MoveEvaluator
from chess_ai.utils import uci_to_move

def main():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    board_manager = BoardManager()
    evaluator = MoveEvaluator()

    while not board_manager.game_over():
        board_manager.show_board()
        legal_moves = board_manager.get_legal_moves()
        best_move, score = evaluator.best_move(board_manager.get_fen(), legal_moves)
        move_obj = uci_to_move(board_manager.board, best_move)
        if move_obj:
            print(f"\nGPT suggests: {best_move} with score {score}\n")
            board_manager.make_move(move_obj)
        else:
            print("No valid move found. Exiting.")
            break

    print("Game Over!")
    board_manager.show_board()

if __name__ == "__main__":
    main()
