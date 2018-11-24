while True:
    pwd=input("nhap password ? ")
    if len(pwd) <8:
        print("not long enough")
    elif pwd.isdigit(): # ktra co phai toan so
        print("not long enough")
    elif pwd.isupper(): # ktra co phai toan chu hoa
        print("must contain lowercase letters")
    elif pwd.islower(): # ktra co phai toan chu thuong
        print("must contain uppercase letters")
    else :
        print("OK")
