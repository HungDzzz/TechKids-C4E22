from random import randint,choice
# neu chi import random thi khi dung phai dung lenh bien = random.choice(list)
while True :
    a = ['+', '-', '*', '/']
    x = randint(0, 10)
    y = randint(1, 10)
    error = randint(-1,1)
    op = choice(a)
    #print(op)
    if op == '+':
        r = x + y + error
    elif op == '-':
        r = x - y + error
    elif op == '*':
        r = x * y + error
    elif op == '/':
        r = x / y + error
    output = "{0} {1} {2} = {3}".format(x, op, y, r)
    print(output)
    users_answer = input("(Y/N) ? ").upper()
    if error == 0:
        if users_answer == 'Y':
            print("Yay")
        else:
            print("Nay")
        print("*"*10)
    else:
        if users_answer == 'N':
            print("Yay")
        else :
            print("Nay")
        print("*"*10)

# # khi goi tu ham khac 
# quiz = generate_quiz()
# x, y, op, r = quiz # return [x, y,op,r] 
# or x,y,op,r = generate_quiz()
# pip install pyqt5