# Credit https://youtu.be/-ivz8yJ4l4E?si=HkWr8uDtmmGKFGvm

import random
import chess
from evaluate import Values


class Minimax:

    def __init__(self, depth, maximizing_color):

        self.depth = depth
        self.alpha = float('-inf')
        self.beta = float('inf')
        self.maximizing_player = True
        self.maximizing_color = maximizing_color


    def _minimax(self, board, depth, alpha, beta, maximizing_player, maximizing_color):
        """
            Minimax algorithm used to find best move for the AI
            :param board: the current board being used for the game (Board)
            :param depth: controls how deep to search the tree of possible moves (int)
            :param alpha: the best value that the maximizer currently can guarantee at that level or above (int)
            :param beta: the best value that the minimizer currently can guarantee at that level or above (int)
            :param maximizing_player: True if current player is maximizing player (bool)
            :param maximizing_color: color of the AI using this function to determine a move (tuple)
            :return: tuple representing move and eval; format: (move, eval)
        """
        if depth == 0 or board.is_game_over():
            return None, Values(board).evaluate(maximizing_color)
        moves = list(board.legal_moves)
        best_move = random.choice(moves)

        if maximizing_player:
            max_eval = float('-inf')
            for move in moves:
                board.push(move)
                current_eval = self._minimax(board, depth - 1, alpha, beta, False, maximizing_color)[1]
                board.pop()
                if current_eval > max_eval:
                    max_eval = current_eval
                    best_move = move
                alpha = max(alpha, max_eval)
                if beta <= alpha:
                    break
            return best_move, max_eval
        else:
            min_eval = float('inf')
            for move in moves:
                board.push(move)
                current_eval = self._minimax(board, depth - 1, alpha, beta, True, maximizing_color)[1]
                board.pop()
                if current_eval < min_eval:
                    min_eval = current_eval
                    best_move = move
                beta = min(beta, min_eval)
                if beta <= alpha:
                    break
            return best_move, min_eval
        

    def minimax(self, board):
        return self._minimax(board, self.depth, self.alpha, self.beta, self.maximizing_player, self.maximizing_color)[0]
