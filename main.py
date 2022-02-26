from turtle import *

jace = Turtle()
des = Turtle()
jabs = Turtle()

print(jace)
jace.shape("turtle")
jace.color("coral")
des.shape("turtle")
des.color("blue")
jabs.shape("turtle")
jabs.color("yellow")
# jace.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

for _ in range(4):
  jace.forward(100)
  jace.left(90)
  des.backward(100)
  des.right(90)
