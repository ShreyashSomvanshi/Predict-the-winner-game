import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
userBet = screen.textinput(title="Make your bet", prompt="Which turtle will in the race? Enter its Color: ")
colors = ["red", "magenta", "blue", "green", "orange", "purple"]
yPos = [-70, -40, -10, 20, 50, 80]
all_turtles = []
newTurtle = Turtle()
newTurtle.speed("fast")
for turtleIndex in range(0, 6):
    newTurtle = Turtle(shape="turtle")
    newTurtle.penup()
    newTurtle.color(colors[turtleIndex])
    newTurtle.goto(x=-230, y=yPos[turtleIndex])
    all_turtles.append(newTurtle)

if userBet:
    isRaceOn = True

while isRaceOn:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            isRaceOn = False
            winnerTurtle = turtle.pencolor()
            if winnerTurtle == userBet:
                print(f"You Won! The {winnerTurtle} turtle is the winner....")
            else:
                print(f"You Lost! The {winnerTurtle} turtle is the winner....")
        rand_Dist = random.randint(0, 10)
        turtle.forward(rand_Dist)
screen.exitonclick()