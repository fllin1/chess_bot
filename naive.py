import chess
import random


def random_board(n=500):
    """
    Create a random situation
    :param board: number of turns (int)
    :return: Board;
    """
    board = chess.Board()
    n_moves = random.randrange(n)
    for _ in range(n_moves):
        if board.is_checkmate():
            return board
        legal_moves = list(board.legal_moves)
        board.push(random.choice(legal_moves))
    return board

def random_move(board):
    """
    Selects a random move from the valid moves for the current players turn
    :param board: the current board being used for the game (Board)
    :return: tuple representing move;
    """
    moves = list(board.legal_moves)
    if moves:
        return random.choice(moves)


def possible_takes (board):
    can_take = []
    """
    Selects a random move from the valid moves for the current players turn
    :param board: the current board being used for the game (Board)
    :return: tuple representing move;
    """
    # Parcourt toutes les pièces de la couleur actuelle
    for piece_type in (chess.PAWN, chess.KNIGHT, chess.BISHOP, chess.ROOK, chess.QUEEN, chess.KING):
        for square in board.pieces(piece_type, board.turn):
            # Parcourt tous les coups légaux pour cette pièce
            for move in board.legal_moves:
                if move.from_square == square and board.is_capture(move):
                    can_take.append(move)
    
    if len(can_take) == 0:
        return random.choice(list(board.legal_moves))
    return random.choice(can_take)