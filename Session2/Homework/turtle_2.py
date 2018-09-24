from turtle import *
shape("turtle")

color("red")
for i in range(4):
    forward(150)
    left(90)

color("blue")
left(60)
forward(150)
left(-120)
forward(150)
left(130)
forward(150)
left(70)
forward(165)
left(80)
forward(165)
left(70)
forward(150)

color("red")
left(70)
forward(150)
for i in range(5):
    left(60)
    forward(150)
mainloop()