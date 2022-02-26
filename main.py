import turtle as t
import random


jace = t.Turtle()
t.colormode(255)

def random_colour():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  random_colour = (r, g, b)
  return random_colour

directions = [0, 90, 100, 270]

# jace.forward(30)
# jace.setheading(random.choice(directions))
print(jace)
jace.shape("turtle")
jace.pensize(15)
jace.speed("fastest")

for _ in range(200):
  jace.color(random_colour())
  jace.forward(30)
  jace.setheading(random.choice(directions))