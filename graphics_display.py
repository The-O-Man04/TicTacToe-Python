import pygame
from board import Board
# pygame.init()
# screen = pygame.display.set_mode(screen_size)


class GraphicDisplay:
    # tuple(nat, nat), Board, Font, nat, nat, Color|Tuple(nat, nat, nat), Color|Tuple(nat, nat, nat)
    def __init__(self, screensize, board, font, line_width=3, margin=10, colour=(255, 255, 255), bg_colour=(0, 0, 0)):
        self.screensize = screensize
        self.x_size = screensize[0]
        self.y_size = screensize[1] * 4 / 5
        self.header_height = screensize[1] / 5
        # self.header_surface = pygame.Surface(self.x_size, self.header_height)
        # self.board_surface = pygame.Surface(self.x_size, self.y_size)
        self.header_rect = pygame.Rect(0, 0, self.x_size, self.header_height)
        self.board_rect = pygame.Rect(0, self.header_height, self.x_size, self.y_size)
        self.board = board
        self.cell_x_size = self.x_size / self.board.size
        self.cell_y_size = self.y_size / self.board.size
        self.screen = pygame.display.set_mode(screensize)
        self.colour = colour
        self.bg_colour = bg_colour
        self.line_width = line_width
        self.margin = margin
        self.font = font

    def display_grid(self):
        for i in range(1, self.board.size):
            pygame.draw.line(self.screen, self.colour, (self.cell_x_size*i, self.header_height),
                             (self.cell_x_size*i, self.y_size + self.header_height), self.line_width)
            pygame.draw.line(self.screen, self.colour, (0, self.header_height + self.cell_y_size*i),
                             (self.x_size, self.header_height + self.cell_y_size*i), self.line_width)
        pygame.display.update()

    def display_cell(self, r, c):  # line width = 3, margin = 10
        if r < 0 or r >= self.board.size or c < 0 or c >= self.board.size:
            raise ValueError()
        if self.board.get_cell_state(r, c) == 'X':  # drawing X
            pygame.draw.line(self.screen, self.colour,
                             ((self.cell_x_size * c) + self.margin, self.header_height + (self.cell_y_size * r) + self.margin),
                             ((self.cell_x_size * (c+1)) - self.margin, self.header_height + (self.cell_y_size * (r+1)) - self.margin),
                             self.line_width)
            pygame.draw.line(self.screen, self.colour,
                             ((self.cell_x_size * (c + 1)) - self.margin, self.header_height + (self.cell_y_size * r) + self.margin),
                             ((self.cell_x_size * c) + self.margin, self.header_height + (self.cell_y_size * (r + 1)) - self.margin),
                             self.line_width)

        elif self.board.get_cell_state(r, c) == 'O':  # drawing O
            pygame.draw.circle(self.screen, self.colour,
                               ((self.cell_x_size * c) + (self.cell_x_size / 2), self.header_height + (self.cell_y_size * r) + (self.cell_y_size / 2)),
                               min(self.cell_x_size, self.cell_y_size) / 2 - self.margin, self.line_width)
        pygame.display.update()

    def clear_display(self, clear_only_cells=True):
        self.screen.fill(self.bg_colour, self.board_rect)
        if clear_only_cells:
            self.display_grid()
        pygame.display.update()

    def display_board(self):  # clears board display, displays grid and all nonempty cells
        self.clear_display()
        self.display_grid()
        for r in range(self.board.size):
            for c in range(self.board.size):
                self.display_cell(r, c)

    def pos_to_cell(self, pos):  # returns which cell the point [pos] lies in
        if pos[1] < self.header_height or pos[0] < 0 or pos[0] > self.x_size or pos[1] > self.y_size+self.header_height:
            raise ValueError()
        j = 0
        temp = pos[0] - self.cell_x_size
        while temp > 0:
            temp -= self.cell_x_size
            j += 1
        i = 0
        temp = pos[1] - self.cell_y_size
        while temp > self.header_height:
            temp -= self.cell_y_size
            i += 1
        return (i, j)

    def display_header(self, message):
        self.screen.fill(self.bg_colour, self.header_rect)
        text = self.font.render(message, True, self.colour)
        self.screen.blit(text, ((self.x_size - text.get_width()) / 2, 0))
        pygame.display.update()

