class TicTacToe:


    def __init__(self):

        self.board = [[""]*3 for i in range(3)]
        self.player = "X"


    def mark(self):
        if self.winner() is not None:
            raise ValueError("game is already complete")
        i = None
        j = None
        for move in range(9):
            self.player = input("enter your move: ")
            index = input("enter the position separated by comma: ")
            position = index.split(",")
            i = int(position[0])
            j = int(position[1])
            if self.player == "X":
                self.player = "O"
            else:
                self.player = "X"

        if self.board[i][j] == " ":
            print("Board position empty")
        elif not (0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError("invalid board position")


    def _iswin_(self,mark):
         board =  self.board
         return (mark == board[0][0] == board[0][1] == board[0][2] or           #first row
                 mark == board[1][0] == board[1][1] == board[1][2] or           #second row
                 mark == board[2][0] == board[2][1] == board[2][2] or           #third row
                 mark == board[0][0] == board[1][0] == board[2][0] or           #first column
                 mark == board[0][1] == board[1][1 == board[2][1]] or           #second column
                 mark == board[0][2] == board[1][2] == board[2][2] or           #third column
                 mark == board[0][0] == board[1][1] == board[2][2] or           #diagonal
                 mark == board[0][2] == board[1][1] == board[2][0])             #reverse diagonal


    def winner(self):
        for mark in "XO":
            if self._iswin_(mark):
                return mark
            return None


    def __str__(self):
        rows = ["|".join(self.board[r]) for r in range(3)]
        return "\n-----\n".join(rows)

if __name__ == "__main__":
    game = TicTacToe()
    game.mark()
    game.winner()