import time
import math
from tic_tac_toe import HumanPlayer, RandomComputerPlayer, UnbeatableComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)] # represents 3x3 matrix
        self.currentWinner = None # track who wins the game 
        
    def print_board(self):
        
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")
            
    @staticmethod
    def printBoardNumber():
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")
            
    def avaliableMoves(self):
        return [i for i, x in enumerate(self.board) if x == " "]

    def empty_squares(self):
        return " " in self.board

    def numsof_empty_sqr(self):
        return self.board.count(" ")
    
    def makeMove(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.currentWinner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # Checking rows
        row_index = math.floor(square / 3)
        row = self.board[row_index*3 : (row_index+1)*3]
        if all(spot == letter for spot in row ):
            return True
        # Checking Columns
        colm_index = square % 3
        column = [self.board[colm_index+i*3] for i in range(3)] 
        if all(spot == letter for spot in column):
            return True
        # Checking Diagonals
        left_to_right = [0, 4, 8]
        right_to_left = [2, 4, 6]
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in left_to_right]
            if all(spot == letter for spot in diagonal1):
                return True       
            diagonal2 = [self.board[i] for i in right_to_left]
            if all(spot == letter for spot in diagonal2):
                return True     
        return False
        
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.printBoardNumber()
    letter = "X" # Def Starting Letter
    while game.empty_squares():
        if letter == "O":
            square = o_player.getMove(game)
        else:
            square = x_player.getMove(game)
        
        if game.makeMove(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}\n")
                game.print_board()
                print("")
            if game.currentWinner:
                if print_game:
                    print(letter + "WINS THE GAME !!!")
                return letter
             
            # Change the player
            if letter == "X":
                letter = "O"
            else:
                letter = "X"
        time.sleep(0.8)
    if print_game:
        print("The game result is TIE !!!")     

if __name__ == "__main__":
    x_wins = 0
    o_wins = 0
    tie = 0
    for _ in range(1000):
        x_player = HumanPlayer("X")
        #o_player = RandomComputerPlayer("O")
        o_player = UnbeatableComputerPlayer("O")
        t = TicTacToe()
        play(t, x_player, o_player, print_game=True)
            
    
    
     
        
        
        