from turtle import Turtle

# Constant values 
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0 

class Snake():
    def __init__(self) -> None:
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

  
    def create_snake(self):
        '''Creation of the snakes'''
        for square in STARTING_POS:
            self.add_segment(square)


    def add_segment(self, square):
        '''Adding a new segment to the snake, making the snake longer'''
        new_square = Turtle('square')
        new_square.color('green')
        new_square.penup()
        new_square.goto(square)
        self.squares.append(new_square)


    def extend(self):
        '''Adds a new segment behind the last segment'''
        self.add_segment(self.squares[-1].position())


    def reset(self):
        '''Moves the old snake out of screen upon death'''
        for square in self.squares:
            square.goto(1000,1000)
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]


    def move(self):
        '''Manages the movement of the snake'''
        for snake in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[snake -1].xcor()
            new_y = self.squares[snake -1].ycor()
            self.squares[snake].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    #Movement of the snake
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    
