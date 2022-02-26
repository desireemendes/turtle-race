# import turtle as t
# import random


# jace = t.Turtle()
# t.colormode(255)

# def random_colour():
#   r = random.randint(0, 255)
#   g = random.randint(0, 255)
#   b = random.randint(0, 255)
#   colour = (r, g, b)
#   return colour

# directions = [0, 90, 100, 270]

# jace.forward(30)
# jace.setheading(random.choice(directions))
# print(jace)
# jace.shape("turtle")
# jace.pensize(15)
# jace.speed("fastest")

# for _ in range(200):
#   jace.color(random_colour())
#   jace.forward(30)
#   jace.setheading(random.choice(directions))

from turtle import Turtle, Screen



jace = Turtle()
screen = Screen()
# image = "race.png"
# screen.addshape(image)
screen.setup(width=500, height=400)
jace.screen.bgcolor("white")
jace.screen.bgpic('sky.gif')
user_bet = screen.textinput(title="Make your bets", prompt="Which turtle will win the race? Enter colour: ")
print(user_bet)


def move_forward():
  jace.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()