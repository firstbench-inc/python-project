"""
Our program, who art in memory,
    called by thy name;
  thy operating system run;
thy function be done at 
  as it was on development.runtime
Give us this day our daily output.
And forgive us our code duplication,
    as we forgive those who
  duplicate code against us.
And lead us not into frustration;
  but deliver us from GOTOs.
    For thine is algorithm,
the computation, and the solution,
    looping forever and ever.
          Return;
"""

import pygame
import game
from pyvidplayer import Video
from time import time_ns


class Button:
    def __init__(self, img_path: str, pos: (int, int)):
        self.image = pygame.image.load(img_path).convert_alpha()
        self.pos = pos
        self.rect = self.image.get_rect(topleft=pos)
        return


def get_board_cord(x: int, y: int) -> (int, int):
    imgx, imgy = 780, 490
    return ((x // 2) - (imgx // 2), (y // 2) - (imgy // 2))


def place_coin(surface, col_no: int, row_no: int, board_pos: (int, int), player: int):
    pos_x = 71 + 106 * (col_no)
    pos_y = 51 + 77 * (row_no)
    if player == 1:
        return pygame.draw.circle(surface, (125, 24, 28), (pos_x, pos_y), 37)
    if player == 2:
        return pygame.draw.circle(surface, (40, 95, 71), (pos_x, pos_y), 37)


def place_timer(surface, player: int, time: int):
    font = pygame.font.Font("freesansbold.ttf", 32)
    if player == 1:
        timer = font.render("player 1: " + str(time), True, (125, 24, 28))
        surface.blit(timer, (100, 5))
    if player == 2:
        timer = font.render("player 2: " + str(time), True, (40, 95, 71))
        surface.blit(timer, (1100, 5))
    return


# ------------ pygame init -------------
pygame.init()

# running = True
screen = pygame.display.set_mode((1366, 780))
# # screen.fill((255, 255, 255))
# clock = pygame.time.Clock()

board = pygame.image.load(r"./assets/board2.png")
bg = pygame.image.load(r"./assets/bg1.jpg")

board_pos = get_board_cord(screen.get_width(), screen.get_height())
vid = Video("./assets/INTRO3.mp4")
vid.set_size((1366, 780))


def intro():
    while True:
        vid.draw(screen, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if (
                event.type == pygame.MOUSEBUTTONDOWN
            ):  # or event.type == pygame.K_RETURN:
                vid.__del__()
                main_game()
                return


def main_game():
    running = True

    clock = pygame.time.Clock()
    # ----------- game init -----------------
    game_state = game.Game()
    coins = []
    timer = time_ns()

    # ------------ columns ------------------
    columns = []
    start_point = board_pos[0] + 32
    for i in range(1, 8):
        columns.append(
            Button(f"assets/button_r ({i}).png", (start_point + 106 * (i - 1), 50))
        )
        pass

    # ------------ game loop ----------------

    screen.blit(bg, (0, 0))
    screen.blits(((col.image, (col.pos[0], col.pos[1])) for col in columns))
    screen.blit(board, board_pos)
    print(game_state.player_turn)
    while running:
        coin_added = False
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))
        screen.blits(((col.image, (col.pos[0], col.pos[1])) for col in columns))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for col_no, col in enumerate(columns):
                    if col.rect.collidepoint(mouse_pos):
                        # user has pressed a column button
                        print(f"col {col_no + 1} was pressed!")
                        player = game_state.player_turn
                        row_no = game_state.add_coin(col_no)
                        if row_no is None:
                            continue
                        row_no = 5 - row_no
                        print(row_no)
                        # create a coin and add it to the list
                        coins.append(
                            # updates the game_state
                            place_coin(
                                board,
                                col_no,
                                row_no,
                                board_pos,
                                player,
                            )
                        )
                        coin_added = True
                        # check for win
                        win = game_state.check_win()
                        if win:
                            print(f"player {win} won!")
                            running = False
                    pass
                pass

        if not coin_added:
            time_left = (time_ns() - timer) // (10**9)
            if time_left > 15:
                print(game_state.player_turn)
                game_state.player_turn = 1 if game_state.player_turn == 2 else 2
                print("player change", game_state.player_turn)
                timer = time_ns()
                place_timer(screen, game_state.player_turn, 15)
            else:
                place_timer(screen, game_state.player_turn, 15 - time_left)
        else:
            timer = time_ns()
            place_timer(screen, game_state.player_turn, 15)
            pass
        screen.blit(board, board_pos)
        pygame.display.update()
        clock.tick(60)
        pass


intro()
