# Importing the important libraries
import os
import random
import turtle 
import winsound
import time

screen = turtle.Screen()
turtle.fd(0)                     # To show the window of the turtle
turtle.speed(0)                  # Set the animation speed to maximum which is 0
turtle.bgcolor("black")
# turtle.bgpic("background1.gif") # Background image
turtle.title("Space Wars")

turtle.ht()
turtle.setundobuffer(1)          # Takes less memory
turtle.tracer(0)

class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1
    
    def move(self):
        self.fd(self.speed)

        # Border Control Reflect
        if self.xcor() > 290:
            self.setx(290)
            self.rt(60)

        if self.xcor() < -290:
            self.setx(-290)
            self.rt(60)

        if self.ycor() > 290:
            self.sety(290)
            self.rt(60)

        if self.ycor() < -290:
            self.sety(-290)
            self.rt(60)
    
    def is_collision(self, other):
        if (self.xcor() >= (other.xcor() - 20)) and \
        (self.xcor() <= (other.xcor() + 20)) and \
        (self.ycor() >= (other.ycor() - 20)) and \
        (self.ycor() <= (other.ycor() + 20)):
            return True
        else:
            return False
        
# Main Game Loop:

while True:
    screen.update()
    time.sleep(0.03)

    