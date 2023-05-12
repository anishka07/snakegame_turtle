from snake_move import Snake
from turtle import Turtle
import random
COLOR = ['red','blue','orange','green','purple','cyan']
SHAPE = ['circle','square','turtle']

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(random.choice(SHAPE))
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color('red')
        self.speed('fastest')
        self.refresh()
    
    def refresh(self):
        self.color(random.choice(COLOR))
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)