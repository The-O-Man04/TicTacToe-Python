from board import Board
# from text_display import TextDisplay
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
# td = TextDisplay(game)
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
            if game_end:
                game.clear()
                gd.clear_display()
                game_end = False
                display_standard_message(x_turn)
            else:
                try:
                    cell = gd.pos_to_cell(pygame.mouse.get_pos())
                except TypeError:
                    pass
                else:
                    print(cell)
                    if game.change_cell(cell[0], cell[1], x_turn):
                        x_turn = not x_turn
                        gd.display_cell(cell[0], cell[1])
                        if game.has_won(not x_turn):
                            if x_turn:
                                print("O wins")
                                gd.display_header("O Wins")
                            else:
                                print("X wins")
                                gd.display_header("X wins")
                            game_end = True
                        elif game.is_full():
                            print("Draw")
                            gd.display_header("Draw")
                            game_end = True
                        else:
                            display_standard_message(x_turn)

    # replace this with GUI
    # if x_turn:
    #    prompt = "X's turn:"
    # else:
    #  prompt = "O's turn:"
    # cmd = input(prompt)
    # if cmd == "move":
    #    r = int(input("row: "))
    #    c = int(input("col: "))
    #    if game.change_cell(r, c, x_turn):
    #        x_turn = not x_turn
    #    if game.has_won(not x_turn):
    #        if x_turn:
    #            print("O wins")
    #        else:
    #            print("X wins")
    #        game.clear()
    #   td.display_board()

    # elif cmd == "clear":
    #    game.clear()
    #    td.display_board()

    # elif cmd == "quit":
    #    done = True
    # else:
    #    print("invalid command")
