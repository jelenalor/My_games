import numpy as np
from optparse import OptionParser

# Allows to parse the parametors via command line
# -n -> sets the number of games you want agent to play
parser = OptionParser()
parser.add_option("-n", "--numGames", dest="num",
                  help="number of games to play")

(options, args) = parser.parse_args()


# import class myGame from file game
from game import myGame


class PlayGames():
    def __init__(self, number_of_games):
        # number of games to play
        self.number_of_games = number_of_games
        # start the game with 'x' player
        self.player = "x"
        # keep track of previous game winner 
        # to ensure this one starts the next game
        self.prev_game_winner = ""
        # Collect statistics about the games
        self.stats = []
        
    def play(self):
        for i in range(self.number_of_games):
            winner = self.playGame(i)
            self.stats.append(winner)
            
    def playGame(self, game_number):
        # initiate new game
        game = myGame()
        if game_number > 0:
            # if game is not the first one, than the previous
            # game winner starts the game
            self.player = self.prev_game_winner
            # while no winner, play game (make move)
        while game._isWin() == False:
            game.makeMove(player = self.player)
            self.swapPlayer()

        # when there is  win -> update the previous game winner
        self.prev_game_winner = game.winner
        return game.winner
    
    def swapPlayer(self):
        if self.player == "o":
            self.player = "x"
        else:
            self.player = "o"
            
    def showStats(self):
        wins, counts = np.unique(np.array(self.stats), return_counts=True)
        for w, c in zip(wins, counts):
            print (w +" - ", + c)

            
if __name__ == '__main__':
    g = PlayGames(int(options.num))
    g.play()
    g.showStats()
    