from players import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # list to rep 3x3 board
        self.current_winner = None # keep track of winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc. tells us what number belong to what box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # returns a list of available moves
        moves = []
        for (i, empty_spot) in enumerate(self.board):
            if empty_spot == ' ':
                moves.append(i)
        return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if valid move, then assign square to letter
        # else if invalid move return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # winner if 3 same letters in a row, column or diagonal

        # first check row
        row_ind = square // 3
        row = self.board[row_ind * 3 : (row_ind + 1) * 3]
        if all([empty_spot == letter for empty_spot in row]):
            return True

        # check column
        col_ind = square % 3
        col = [self.board[col_ind+i * 3] for i in range(3)]
        if all([empty_spot == letter for empty_spot in col]):
            return True

        # check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] #left to right diagonal
            if all([empty_spot == letter for empty_spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]] # right to left diagonal
            if all([empty_spot == letter for empty_spot in diagonal2]):
                return True

        # if all these fail return False
        return False



def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter
    # keep iterating while the game still has empty squares
    while game.empty_squares():
        # get the move from the player who has the turn
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # define a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') # just empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter


            # after move is made letters need to be alternated
            letter = 'O' if letter == 'X' else 'X' # switches player

    if print_game:
        print("It's a tie!")

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)