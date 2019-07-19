import random

class Game():
    def __init__(self):
        # start a game by player 1
        self.player = 1
        self.win = False
        self.winner = 0
        
    def switchPlayer(self):
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1
            
    def makeRandomMove(self, available_cols):
        col = random.choice(available_cols)
        return col
    
    def makeHumanMove(self, available_cols):
        while True:
            move = int(input("%s Choose column between 0 and 6: " %self.player))
            if move in available_cols:
                print("Move accepted")
                break
                
            elif move > 6:
                print("Invalid column, %s choose another column" %self.player)
                continue

            else:
                print("Column is full, %s choose another column" %self.player)
                continue
        return move
    
    def play(self):
        # start a game by instiating an environment (grid)
        grid = Env()
        
        while self.win == False:
            # find available columns to play
            available_moves = grid.availableMoves()
            # get a move
            # if list of moves is empty -> draw
            if len(available_moves) == 0:
                print("It is a draw")
                break
                
            column = self.makeHumanMove(available_moves)
            #return an available row for a choosen column
            row = grid.returnRow(column)
            # Update grid with the move
            move = [row, column]
            grid.updateGrid(move, self.player)
            grid.displayGrid()
            self.win = grid.checkWin(move)[0]
            print(self.win)
            if self.win == True:
                self.winner = grid.checkWin(move)[1]
                print("Winner is ", self.winner)
                break
            else:
                self.switchPlayer()
            
class Env():
    def __init__(self):
        # Create a grid nrows = 6, ncols = 7, zero = empty space
        self.grid = []
        for i in range(6):
            self.grid.append([0]*7)
    
    def updateGrid(self, move, player):
        # move = [list, item] - [row, col]
        # player = either 1 or 2
        self.grid[move[0]][move[1]] = player
        
    def returnRow(self, col):
        #return the row for col move, e.g. check how many rows are taken in this column
        # 6 rows - iterate over all rows for specified column until find there non zero cell (taken)
        # return the row before that as a available for move and stop iterating
        for i in range(6):
            if self.grid[i][col] != 0:
                clear_row = i-1
                return clear_row
                break
            elif i == 5 and self.grid[i][col] == 0:
                clear_row = 5
                return clear_row
            
            elif i == 0 and self.grid[i][col] != 0:
                # -1 corresponds to the full columns
                clear_row = -1
                return clear_row
            
    def availableMoves(self):
        available_cols = []
        # iterate over all columns if not full, add to available columns
        for i in range(7):
            if self.returnRow(i) != -1:
                available_cols.append(i)
        return available_cols
        
    def displayGrid(self):
        for i in self.grid:
            print(i)
            
    def checkWin(self, move):
        value = self.grid[move[0]][move[1]]
        win = False

        #horizontal check
        counter = 0
        for i in range(move[1]+1, min(7, move[1]+4)):
            if self.grid[move[0]][i] == value:
                counter += 1
                if counter == 3:
                    win = True
                    return win, value
            else:
                break     

        for i in range(max(0, move[1]-3), move[1])[::-1]:
            if self.grid[move[0]][i] == value:
                counter += 1
                if counter == 3:
                    win = True
                    return win, value
            else:
                break


        #vertical check
        counter = 0
        for i in range(move[0]+1, min(6, move[0]+4)):
            if self.grid[i][move[1]] == value:
                counter += 1
                if counter == 3:
                    win = True
                    return win, value 
            else:
                break     
        for i in range(max(0, move[0]-3), move[0])[::-1]:
            if self.grid[i][move[1]] == value:
                counter += 1
                if counter == 3:
                    win = True
                    return win, value
            else:
                break

        #diagonal NE
        # row decreases (i) - col (j) increases; OR ;row (i) increases - col (j) decreases 
        counter = 0
        i = move[0]-1
        j = move[1]+1
        while i >= max(0, move[0]-3) and j <= min(6, move[1]+3):  

            if self.grid[i][j] == value:
                counter += 1
                i -= 1
                j += 1
                if counter == 3:
                    win = True
                    return win, value  
            else:
                break

        i = move[0]+1
        j = move[1]-1
        while i <= min(5, move[0]+3) and j >= max(0, move[1]-3):  
            if self.grid[i][j] == value:
                counter += 1
                i += 1
                j -= 1
                if counter == 3:
                    win = True
                    return win, value 
            else:
                break

        #diagonal NW
        # row increases (i) - col (j) increases; OR ;row (i) decreases - col (j) decreases 
        counter = 0
        i = move[0]+1
        j = move[1]+1
        while i <= min(5, move[0]+3) and j <= min(6, move[1]+3):  
            if self.grid[i][j] == value:
                counter += 1
                i += 1
                j += 1
                if counter == 3:
                    win = True
                    return win, value 
            else:
                break

        i = move[0]-1
        j = move[1]-1
        while i >= max(0, move[0]-3) and j >= max(0, move[1]-3):  
            if self.grid[i][j] == value:
                counter += 1
                i -= 1
                j -= 1
                if counter == 3:
                    win = True
                    return win, value  
            else:
                return win, "no winner"
                
        return win, "no winner"
            
    
if __name__ == '__main__':
    g = Game()
    g.play()