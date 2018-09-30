items = ['com','pho','my']
print(*items,sep='\n')

while True:
    i = int(input("nhap vao vi tri ban muon xem : "))
    if -3 <= i <=3 :
        print(items[i-1])
        break
    else:
        print("vi tri khong ton tai")