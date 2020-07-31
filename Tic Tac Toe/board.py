from datetime import datetime
from datetime import date


class Board:
    board = None

    def __init__(self, board_size):
        self.create_empty_board(board_size)
        print(f"Created an empty board at {get_current_time()}.")
    
    def create_empty_board(self, size):
        self.board = [["" for k in range(size)] for i in range(size)]


# gets current time and returns it as a string
def get_current_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.today().strftime("%d/%m/%Y")

    return f"{current_time} {current_date}"
    
