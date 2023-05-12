x = [(0,0),(0,-20),(0,-40)]
COLOR = ['red','blue','orange','green','purple','cyan','yellow','white',]
SHAPE = ['circle','square','turtle']
MOVE_DSTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
from turtle import Turtle
import random

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for i in x:
            self.add_segments(i)
    
    def snake_reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    
    def add_segments(self,i):
            snake = Turtle('square')
            snake.color(random.choice(COLOR))
            snake.penup()
            snake.setpos(i)
            self.segments.append(snake)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            self.segments[seg].goto(self.segments[seg-1].xcor(),self.segments[seg-1].ycor())
        self.head.fd(MOVE_DSTANCE)
    
    def up(self):
        if self.head.heading()!=DOWN:
          self.head.setheading(UP)
          
    def down(self):
        if self.head.heading()!=UP:
          self.head.setheading(DOWN)

    def right(self):
        if self.head.heading()!=LEFT:
          self.head.setheading(RIGHT)

    def left(self): 
        if self.head.heading()!=RIGHT:
          self.head.setheading(LEFT)