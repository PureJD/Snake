from turtle import Turtle

SCORE_LOCATION = (0, 250)



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__() 
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(SCORE_LOCATION)
    
    def score_write(self, player_score):
        self.clear()
        self.write( arg= (f'Score: {player_score} ') , move= False, align= 'center', font= ('courier', 20, 'normal'))
        
    def game_over(self, player_score):
        self.clear()
        self.goto(0,0)
        self.write( arg= (f'Game over, you finish with a score of: {player_score} ') , move= False, align= 'center', font= ('courier', 15, 'normal'))
