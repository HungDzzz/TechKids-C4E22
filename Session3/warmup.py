while True:
    yob_str=input("enter your of birth ? ")
    if yob_str.isdigit(): # .isdigit() ktra only number
        yob= int(yob_str)
        age= 2018-yob
        print(age)
        break
    else:
        print("not a number")