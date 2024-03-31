from board import Board
from graphics_display import GraphicDisplay
import pygame
pygame.init()


def display_standard_message(x_turn):
    if x_turn:
        gd.display_header("X to move")
    else:
        gd.display_header("O to move")


screen_size = screen_width, screen_height = 650, 650
clock = pygame.time.Clock()
font = pygame.font.SysFont("Roboto-Regular", 48)

x_turn = True
game = Board()  # default: size = 3, moves to win = 3
gd = GraphicDisplay(screen_size, game, font)
gd.display_grid()
display_standard_message(x_turn)
done = False
game_end = False

while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_end:  # click to clear board when game is done
                game.clear()
                gd.clear_display()
                game_end = False
                display_standard_message(x_turn)
            else:
                try:  # check if click is within region of board
                    cell = gd.pos_to_cell(pygame.mouse.get_pos())
                except ValueError:
                    pass
                else:
                    if game.change_cell(cell[0], cell[1], x_turn):  # false if cell is not empty
                        x_turn = not x_turn
                        gd.display_cell(cell[0], cell[1])
                        if game.has_won(not x_turn):
                            if x_turn:
                                gd.display_header("O Wins")
                            else:
                                gd.display_header("X wins")
                            game_end = True
                        elif game.is_full():
                            gd.display_header("Draw")
                            game_end = True
                        else:
                            display_standard_message(x_turn)
