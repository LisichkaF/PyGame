from pieces.Piece import Piece


class Rook(Piece):
    def __init__(self, color, position):
        self.name = 'Rook'
        super(Rook, self).__init__(color, position)
        if self.color == 'w':
            self.image = 'data/images/WhiteTower.png'
        else:
            self.image = 'data/images/BlackTower.png'

        self.value = 5

    def get_possible_moves(self, board):
        return self.get_possible_straight_line_moves(board)

