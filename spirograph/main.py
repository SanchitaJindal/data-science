import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########
for i in range(18):
  tim.color(random_color())
  tim.circle(10)
  tim.right(20)

s=t.Screen()
s.exitonclick()
