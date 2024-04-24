from turtle import Turtle

SCORE_LOCATION = (0, 250)
HIGHSCORE_LOCATION = (100, 250)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__() 
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(SCORE_LOCATION)
    

    def score_write(self, player_score, high_score_record):
        '''This function will post the player score and highscore to the screen'''
        self.goto(SCORE_LOCATION)
        self.clear()
        self.write( arg= (f'Score: {player_score} | HighScore: {high_score_record} ') , move= False, align= 'center', font= ('courier', 20, 'normal'))
        

    def game_over(self, player_score):
        '''This function will display the player score to the middle of the screen upon death'''
        self.clear()
        self.goto(0,0)
        self.write( arg= (f'Game over, you finish with a score of: {player_score} ') , move= False, align= 'center', font= ('courier', 15, 'normal'))


    def check_highscore(self):
        '''This function will open the highscore text file and determine if there is a score. It will default to zero if not'''
        try:
            with open('highscore.txt', 'r') as file:
                high_score = int(file.read().strip())  
        except FileNotFoundError:
            high_score = 0   
        return high_score


    def update_highscore(self, currrent_score, high_score):
        '''This function opens the highscore file and updates the value if the player has exceeded the highscore.'''
        if currrent_score > high_score:
            with open('highscore.txt', 'w') as file:
                file.write(str(currrent_score))
            print(f'NEW HIGH SCORE! {currrent_score}')
        else:
            print(f'High score unchanged at {currrent_score}')

        