import chess

def uci_to_move(board, uci_str):
    try:
        return chess.Move.from_uci(uci_str)
    except:
        return None
