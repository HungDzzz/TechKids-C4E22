from turtle import *
def draw_square(length,colors):
    color(colors)
    for i in range(4):
        forward(length)
        left(90)
    #mainloop()
#draw_square(150, "red")