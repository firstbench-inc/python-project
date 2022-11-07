class Game:
    def __init__(self) -> None:
        self.board = [[0 for _ in range(7)] for _ in range(6)]
        self.player_turn = 1

    def add_coin(self, col_no):
        if col_no > 6:
            return
        # check if top row is already full
        if self.board[-1][col_no] != 0:
            return

        row = 0
        while self.board[row][col_no] != 0:
            row += 1
            pass
        self.board[row][col_no] = self.player_turn
        self.player_turn = 2 if self.player_turn == 1 else 1
        return row

    def show_board(self):
        for i in self.board[::-1]:
            print(i)

    def check_win(self):
        """check for win condition on the board"""
        win = 0

        for row_no in range(-1, -7, -1):
            for col_no in range(4):
                if (
                    self.board[row_no][col_no]
                    == self.board[row_no][col_no + 1]
                    == self.board[row_no][col_no + 2]
                    == self.board[row_no][col_no + 3]
                ):
                    win = self.board[row_no][col_no]
                    break
            if win:
                break
        if not win:
            for col_no in range(7):
                for row_no in range(-1, -4, -1):
                    if (
                        self.board[row_no][col_no]
                        == self.board[row_no - 1][col_no]
                        == self.board[row_no - 2][col_no]
                        == self.board[row_no - 3][col_no]
                    ):
                        win = self.board[row_no][col_no]
                        break
                if win:
                    break
        if not win:
            for col_no in range(4):
                for row_no in range(-1, -4, -1):
                    if (
                        self.board[row_no][col_no]
                        == self.board[row_no - 1][col_no + 1]
                        == self.board[row_no - 2][col_no + 2]
                        == self.board[row_no - 3][col_no + 3]
                    ):
                        win = self.board[row_no][col_no]
                        break
                if win:
                    break
        if not win:
            for col_no in range(-1, -5, -1):
                for row_no in range(-1, -4, -1):
                    if (
                        self.board[row_no][col_no]
                        == self.board[row_no - 1][col_no - 1]
                        == self.board[row_no - 2][col_no - 2]
                        == self.board[row_no - 3][col_no - 3]
                    ):
                        win = self.board[row_no][col_no]
                        break
                if win:
                    break

        return win
