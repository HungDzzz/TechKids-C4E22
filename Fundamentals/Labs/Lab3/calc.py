def add(x, y): # def la de khai bao func
    r = x + y
    return r # de cho r thoat ra khoi def
# t = add(2,3)
# print(t)
def eval(x, y, op):
    if op == '+':
        r = x+y # return x+y 
        # khi dung return = dung ham k chay nua
    elif op == '-':
        r = x-y
    elif op == '*':
        r = x*y
    elif op == '/':
        r = x/y
    output = "{0} {1} {2} = {3}".format(x, op, y, r)
    return r
# x = int(input("Nhap x : "))
# y = int(input("Nhap y : "))
# op = input("+, -, *, / : ")
# r=eval(x,y,op)
# print(r)
# #print(eval(x,y,op))
