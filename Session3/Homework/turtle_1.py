from turtle import *
shape("turtle")
colors = ['red','blue','brown','yellow','grey']
for i in range(3,8):
    color(colors[i-3])
    for _ in range(i):
        forward(150)
        left(360/(i))
mainloop()