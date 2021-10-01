class Board:
    board = None

    def __init__(self, board_size):
        self.create_empty_board(board_size)
    
    def create_empty_board(self, size):
        self.board = [["" for k in range(size)] for i in range(size)]
