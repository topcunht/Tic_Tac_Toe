import math
import random

class Player:
    def __init__(self, letter):
        # player will be X or O 
        self.letter = letter
    def getMove(self, game):
        pass
    
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def getMove(self, game):
        square = random.choice(game.avaliableMoves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def getMove(self, game):
        valid_square = False
        human_value = None
        while not valid_square:
            human_square = input(self.letter + "\'s turn. Make a choce input (0,8):")
            
            try:
                human_value = int(human_square)
                if human_value not in game.avaliableMoves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square is choosed. Try again.")
        return human_value
    
class UnbeatableComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def getMove(self, game):
        if len(game.avaliableMoves())==9:
            square = random.choice(game.avaliableMoves())
        else:
            # get the square bby minimax algo
            square = self.minimax(game, self.letter)["position"]
        return square
    def minimax(self, state, player):
        max_player = self.letter
        if player == "X":
            other_player = "O"
        else:
            other_player = "X"            
        if state.currentWinner == other_player:
            return {
                "position " : None,
                'score' : 1*(state.numsof_empty_sqr() + 1) if other_player == max_player else -1*(state.numsof_empty_sqr() + 1)
            }
    
        elif not state.empty_squares():
            return {"position": None, 'score' : 0}
        
        if player == max_player:
            best = {"position": None, 'score': -math.inf}
        else:
            best = {"position": None, "score": math.inf}

        for possible_move in state.avaliableMoves():
            state.makeMove(possible_move, player)
            sim_score = self.minimax(state,other_player)
            state.board[possible_move] = " "
            state.currentWinner = None
            sim_score["position"] = possible_move
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best                 
        