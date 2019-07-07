class Grid():
    def __init__(self):
        self.grid = []
        #
        # Create a grid, which is a list of lists
        # each initiated with 3 "*"
        #
        for i in range(3):
            row = ["*"]*3
            self.grid.append(row)
            
    def updateGrid(self, move, player):
        if player == "o":
            self.grid[move[0]][move[1]] = "o"
        else:
            self.grid[move[0]][move[1]] = "x"
        return self.grid
    
    def checkForWin(self):
        win = False
        # check rows
        for row in range(3):
            #
            # if there is only one unique value in the row ("set()")
            # and this unique value is not "*"
            # there is a win
            #
            if len(list(set(self.grid[row]))) == 1 and list(set(self.grid[row]))[0] != "*":
                win = True  

        # check column
        for col in range(3):
            # Extract column data by iterating through lists
            column = []
            for row in range(3):
                column.append(self.grid[row][col])
            #
            # Column check follows the same logic as above
            #
            if len(list(set(column))) == 1 and list(set(column))[0] != "*":
                win = True  

        # check cross
        cross = []
        for i in range(3):
            cross.append(self.grid[i][i])
        if len(list(set(cross))) == 1 and list(set(cross))[0] != "*":
            win = True
        # 2
        cross = []
        for i, j in zip(range(3), range(3)[::-1]):
            cross.append(self.grid[i][j])
        if len(list(set(cross))) == 1 and list(set(cross))[0] != "*":
            win = True
        return win
    
    
    def getLegalMoves(self):
        legal_moves = []
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == "*":
                    legal_moves.append(tuple([i, j])) 
        return legal_moves
    