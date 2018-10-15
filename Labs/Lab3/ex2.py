#import calc
from calc import eval, add # chi can goi eval() , imort * = tat ca
x = int(input("Nhap x : "))
y = int(input("Nhap y : "))
op = input("+, -, *, / : ")
r=eval(x,y,op)
print(r)