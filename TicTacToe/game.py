from game_grid import Grid
from game_move import Random

class myGame():
    def __init__(self):
        self.move = []
        self.end = False
        self.grid = Grid()
        self.winner = ""
    
    def makeMove(self, player):
        #
        # Get the move if there are available moves left
        #
        if len(self.grid.getLegalMoves()) > 0:
            #
            # To make a move we use "Random" class from file "game_move.py"
            # It chooses the random move from the available moves
            # We get available moves from the "Grid" class from "game_grid.py" file
            #
            self.move = Random.getMove(self.grid.getLegalMoves())
            #
            # After the move is chosen, we update the grid
            #
            self.grid.updateGrid(self.move, player)
            #
            # Check for win after each move
            # If won, update the winner
            #
            if self.grid.checkForWin():
                self.end = True
                self.winner = player  
        else:  
            #
            # If no available moves left and no win -> means a draw
            #
            self.end = True    
            self.winner = "draw"
    
    def returnGrid(self):
        return self.grid
            
    def _isWin(self):
        return self.end
    
    def winner(self):
        return self.winner
