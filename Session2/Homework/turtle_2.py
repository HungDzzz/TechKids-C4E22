from turtle import *
shape("turtle")

for i in range(4):
    if i%2==0 :
        color("red")
        for _ in range(6-i):
            forward(150)
            left(360/(6-i))
    else :
        color("blue")
        if i==1 :
            for _ in range(6-i):
                forward(150)
                left(360/(6-i))
        else:
            color("red")
            forward(150)
            color("blue")
            for _ in range(2):
                left(120)
                forward(150)
left(120)
color("red")
mainloop()