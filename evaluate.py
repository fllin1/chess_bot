import chess


class Values:

    def __init__(self, board):

        self.w_piece_values = {
            'P': 10, 'N': 30, 'B': 30, 'R': 50, 'Q': 90, 'K': 900
            }
        self.b_piece_values = {
            'p': 10, 'n': 30, 'b': 30, 'r': 50, 'q': 90, 'k': 900
            }

        self.whiteScore = sum([self.w_piece_values[str(piece)] for piece in board.piece_map().values() if str(piece) in self.w_piece_values])
        self.blackScore = sum([self.b_piece_values[str(piece)] for piece in board.piece_map().values() if str(piece) in self.b_piece_values])

        self.board = board.copy()

    def current_score(self):
        """
        Returns the current scores
        :return: whiteScore, blackScore
        """
        return self.whiteScore, self.blackScore
    
    def evaluate(self, maximizing_color):
        """
        Provides a number representing the value of the board at a given state
        :param board: the current board being used for the game (Board)
        :param maximizing_color: color associated with maximizing player (tuple)
        :return: integer representing boards value
        """
        if maximizing_color == True:
            score = self.whiteScore - self.blackScore
            if self.board.is_check() and self.board.turn == maximizing_color:
                score -= 900
            elif self.board.is_check():
                score += 900
            return score
        else:
            score = self.blackScore - self.whiteScore
            if self.board.is_check() and self.board.turn == maximizing_color:
                score += 900
            elif self.board.is_check():
                score -= 900
            return score
