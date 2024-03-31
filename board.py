class Cell:
    # (nat, nat)
    def __init__(self, pos):
        # add assertion here
        self.row = pos[0]
        self.col = pos[1]
        self.state = '_'  # one of ('_','X','O')

    def get_state(self):
        return self.state

    def cell_is_empty(self):
        if self.state == '_':
            return True
        else:
            return False

    def update_cell(self, x_turn):
        assert self.state == '_' or self.state == 'X' or self.state == 'O'
        if self.cell_is_empty():
            if x_turn:
                self.state = 'X'
            else:
                self.state = 'O'
            return True
        else:
            return False

    def clear_cell(self):
        self.state = '_'


class Board:
    def __init__(self, size=3, cells_to_win=3):
        self.size = size
        self.cells_to_win = cells_to_win
        self.board = []
        for i in range(self.size):
            self.board.append([])
            for j in range(self.size):
                self.board[i].append(Cell((i, j)))

    def get_size(self):
        return self.size

    def clear(self):
        for i in range(self.size):
            for j in range(self.size):
                self.board[i][j].clear_cell()

    def change_cell(self, r, c, x_turn):  # might change params
        assert r >= 0
        assert c >= 0
        assert r < self.size
        assert c < self.size
        return self.board[r][c].update_cell(x_turn)

    def has_won(self, x_turn):
        if x_turn:
            target = 'X'
        else:
            target = 'O'

        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c].get_state() == target:
                    won = True
                    for i in range(1, self.cells_to_win):  # check row
                        if r + i >= self.size or self.board[r + i][c].get_state() != target:
                            won = False
                            break
                    if won:
                        return True
                    won = True
                    for i in range(1, self.cells_to_win):  # check column
                        if c + i >= self.size or self.board[r][c + i].get_state() != target:
                            won = False
                            break
                    if won:
                        return True
                    won = True
                    for i in range(1, self.cells_to_win):  # check down-right diagonal
                        if r + i >= self.size or c + i >= self.size or self.board[r + i][c + i].get_state() != target:
                            won = False
                            break
                    if won:
                        return True
                    won = True
                    for i in range(1, self.cells_to_win):  # check down-left diagonal
                        if r + i >= self.size or c - i < 0 or self.board[r + i][c - i].get_state() != target:
                            won = False
                            break
                    if won:
                        return True

    # returns the cell state ('_', 'X', 'O') or returns '' if input is invalid
    def get_cell_state(self, r, c):
        if 0 <= r and 0 <= c and r < self.size and c < self.size:
            return self.board[r][c].get_state()
        else:
            return ''

    def is_full(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c].get_state() == '_':
                    return False
        return True
