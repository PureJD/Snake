from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# All screen class object changes
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0) # Turns off the auto update


# Creation of objects
snake = Snake()
food = Food()
score = Scoreboard()

# The listening for user input which is constant even out of the loop
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


def main_game_funcation():
    '''This is the main game function. The game has been placed into a function in order to recall'''
    high_score_record = score.check_highscore()
    player_score = 0
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        score.score_write(player_score, high_score_record)
        
        #Collision with food
        if snake.head.distance(food) < 18:
            snake.extend()
            food.refresh()
            player_score += 1
            score.score_write(player_score, high_score_record)

        #Collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            score.game_over(player_score)
            screen.update()
            time.sleep(2)
            score.update_highscore(player_score, high_score_record)
            score.score_write(player_score, high_score_record)
            snake.reset()
            main_game_funcation()
        
        #Collision with tail 
        for square in snake.squares[1::]:
            if snake.head.distance(square) < 10:
                game_is_on = False
                score.game_over(player_score)
                screen.update()
                time.sleep(2)
                score.score_write(player_score, high_score_record)
                score.update_highscore(player_score, high_score_record)
                snake.reset()
                main_game_funcation()

# Technically the main game loop 
while True:         
    main_game_funcation()
    screen.exitonclick()