import random

class Maze:

        
    def __init__(self):
        self.grid = [[{"north": False, "south": False, "east": False, "west": False} for _ in range(8)] for   _ in range(8)] 
        self.visited = []
        self.generate(0,0)
        self.exit = (7, 7)
        self.player_pos = (0, 0)   
        
    def generate(self, row, col):
        self.visited.append((row,col))
        directions = ["north", "south", "east", "west"] 
        random.shuffle(directions)
        moves = {
            "north": (row - 1, col),
            "south": (row + 1, col),
            "east": (row, col + 1),
            "west": (row, col - 1)
        }
        opposite = {"north": "south", "south": "north", "east": "west", "west": "east"} 
        for direction in directions:
            neibhor = moves.get(direction)
            if neibhor not in self.visited:
                if 0 <= neibhor[0] <= 7 and 0 <= neibhor[1] <= 7:
                    self.grid[row][col][direction] = True
                    self.grid[neibhor[0]][neibhor[1]][opposite[direction]] = True
                    self.generate(neibhor[0], neibhor[1])
        
    def display(self):
        for row in range(8):
            for col in range(8):
                print("+", end="")
                if self.grid[row][col]["north"] is False:
                    print("---", end="")
                elif self.grid[row][col]["north"] is True:
                    print("   ", end="")
            print("+")   
            
            for col in range(8):
                if self.grid[row][col]["west"] is False:
                    print("|", end="")
                elif self.grid[row][col]["west"] is True:
                    print(" ", end="")
                print("   ", end="")
            print("|")

        row = 7
        for col in range(8):
            print("+", end="")
            if self.grid[row][col]["south"] is False:
                print("---", end="")
            elif self.grid[row][col]["south"] is True:
                print("   ", end="")
        print("+")

    def move(self):
        row, col = self.player_pos
        pl_direct = input("What dirction(north, south, east, west): ")
        if pl_direct == "north":
            if self.grid[row][col][pl_direct] == True:
                self.player_pos = row-1, col
            else:
                print("error tring to go through closed wall when you are not a ghost!")
        elif pl_direct == "south":
            if self.grid[row][col][pl_direct] == True:
                self.player_pos = row+1, col
            else:
                print("error tring to go through closed wall when you are not a ghost!")
        elif pl_direct == "east":
            if self.grid[row][col][pl_direct] == True:
                self.player_pos = row, col+1
            else:
                print("error tring to go through closed wall when you are not a ghost!")
        elif pl_direct == "west":
            if self.grid[row][col][pl_direct] == True:
                self.player_pos = row, col-1
            else:
                print("error tring to go through closed wall when you are not a ghost!")
        if self.player_pos == self.exit:
            print("Congrats! You Escaped!")
            return

    def play (self):
        self.display()
        while self.player_pos != self.exit:
            self.move()


    