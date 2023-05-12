from turtle import Screen
import time
from snake_move import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Py Snake Game') 
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# KEY FUNCTIONALITIES

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    
# WHEN SNAKE EATS THE FOOD

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.point()
    
# COLLISION IN THE WALL

    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        scoreboard.reset_scoreboard()
        snake.snake_reset()
# COLLISION AGAINST THE TAIL

    for segments in snake.segments[1:]:
        if snake.head.distance(segments)<10:
            scoreboard.reset_scoreboard()
            snake.snake_reset()
screen.exitonclick()
