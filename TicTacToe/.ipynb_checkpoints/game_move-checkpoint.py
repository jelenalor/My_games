import random

class Random():
    def getMove(legal_moves):
        move = random.choice(legal_moves)
        return move