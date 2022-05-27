
import turtle
import time
import random

wn = turtle.Screen()
wn.title("TETRIS")
wn.bgcolor("NavajoWhite2")
wn.setup(width=600, height=800)
wn.tracer(0)
delay = 0.1

class Shape():
    def __init__(self):
        self.x = 5
        self.y = 0
        self.color = random.randint(1,7)

        #Block Shape
        square = [[1,1],
                    [1,1]]

        horizontal_line = [[1,1,1,1,]]

        vertical_line = [[1],
                         [1],
                         [1],
                         [1]]
        
        left_l = [[1,0,0,0],
                  [1,1,1,1]]
        
        right_l = [[0,0,0,1],
                   [1,1,1,1]]

        left_s = [[1,1,0],
                  [0,1,1]]

        right_s = [[0,1,1],
                   [1,1,1]]

        t = [[0,1,0],
             [1,1,1]]

        shapes = [square, horizontal_line, vertical_line, left_l, right_l, left_s, right_s, t]

        #Choose a random shape each time
        self.shape = random.choice(shapes)

        self.height = len(self.shape)
        self.width = len(self.shape[0])      

    def move_left(self, grid):
        if self.x > 0:
            if grid[self.y][self.x - 1] == 0:
                self.erase_shape(grid)
                self.x -= 1

    def move_right(self, grid):
        if self.x < 12 - self.width:
            if grid[self.y][self.x + self.width] == 0:
                self.erase_shape(grid)
                self.x += 1     

    def draw_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if(self.shape[y][x]==1):
                    grid[self,y + y][self.x + x] = self.color

    def erase_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if(self.shape[y][x] -- 1):
                    grid[self.y + y][self.x + x] = 0
    def can_move(self, grid):
        result = True 
        for x in range(self.width):
            if(self.shape[self.height-1][x] == 1):
                if(grid[self.y + self.height][self.x + x] 1 = 0):
                    result = False
        return result         