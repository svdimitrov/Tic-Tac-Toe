import datetime
import os
import pygame
from board import Board

pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (750, 250)

BOARD_SIZE = 3
SCREEN_SIZE = (400, 450)  # y must be greater than x
BOARD_IMAGE = pygame.image.load(r"img/board.png")
ICON_IMAGE = pygame.image.load(r"img/icon.png")
PLAYER_1 = pygame.image.load(r"img/X.png")
PLAYER_2 = pygame.image.load(r"img/O.png")
FONT = pygame.font.SysFont('Comic Sans MS', 30)
PLAYER1_NAME = "Player One"
PLAYER2_NAME = "Player Two"


def start_game():

    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_icon(ICON_IMAGE)
    pygame.display.set_caption("Tic Tac Toe")
    game_board = Board(BOARD_SIZE)
    board = game_board.board
    clock = pygame.time.Clock()
    running = True
    player1_turn = True
    move_has_been_made = False
    game_over = False
    tie = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and not game_over and not tie:
                x_position, y_position = pygame.mouse.get_pos()
                offset = SCREEN_SIZE[1] - SCREEN_SIZE[0]
                distance = SCREEN_SIZE[0] / 3

                if x_position >= 0 and x_position <= SCREEN_SIZE[0] and y_position >= (SCREEN_SIZE[1] - SCREEN_SIZE[0]) and y_position <= SCREEN_SIZE[1]:
                    row = int((y_position - offset) / distance)
                    column = int(x_position / distance)

                    if board[row][column] == "":
                        if player1_turn:
                            board[row][column] = "X"
                        else:
                            board[row][column] = "O"

                        move_has_been_made = True

            clock.tick(60)
            update_screen(screen, board, player1_turn, game_over, tie)

            if move_has_been_made:
                if check_for_winner(board):
                    game_over = True
                elif check_for_tie(board):
                    tie = True
                elif player1_turn:
                    player1_turn = False
                else:
                    player1_turn = True

                move_has_been_made = False


def update_screen(screen, board, player1_turn, game_over, tie):
    screen.fill((220, 220, 200))
    screen.blit(BOARD_IMAGE, (0, 50))
    draw_board(screen, board)
    display_player_name(screen, player1_turn, game_over, tie)
    pygame.display.update()


def display_player_name(screen, player1_turn, game_over, tie):
    if tie:
        text_surface = FONT.render("Tie!", False, (0, 0, 0))
    elif player1_turn:
        if game_over:
            text_surface = FONT.render(
                f"{PLAYER1_NAME} wins!", False, (0, 0, 0))
        else:
            text_surface = FONT.render(
                f"{PLAYER1_NAME}'s turn", False, (0, 0, 0))
    else:
        if game_over:
            text_surface = FONT.render(
                f"{PLAYER2_NAME} wins!", False, (0, 0, 0))
        else:
            text_surface = FONT.render(
                f"{PLAYER2_NAME}'s turn", False, (0, 0, 0))

    screen.blit(text_surface, (0, 0))


def draw_board(screen, board):
    y = 50

    for row in board:
        x = 0
        for cell in row:
            if cell == "X":
                screen.blit(PLAYER_1, (x, y))
            elif cell == "O":
                screen.blit(PLAYER_2, (x, y))
            x += 133
        y += 133


def check_for_winner(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != "":
            return True

    for index in range(len(board[0])):
        if board[0][index] == board[1][index] == board[2][index] != "":
            return True

    if (board[0][0] == board[1][1] == board[2][2] != "") or (board[0][2] == board[1][1] == board[2][0] != ""):
        return True

    return False


def check_for_tie(board):
    tie = True

    for row in board:
        for cell in row:
            if cell == "":
                tie = False

    return tie


# gets current time and returns it as a string
def get_current_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.today().strftime("%d/%m/%Y")

    return f"{current_time} {current_date}"


start_game()
