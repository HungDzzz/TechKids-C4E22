items = ['com','pho','my','bun']
print(items)
#update
# i = int(input("nhap vao vi tri ban muon thay :"))
# txt = input("nhap mon ban muon thay :")
# items[i]=txt
# print(items)
#delete
i = input("ban muon xoa gi :")
if i.isdigit():
    i_ = int(i)
    if i_> len(items):
        print("error")
    else:
        items.pop(i_-1)
        print(items)
else :
    items.remove(i)
    print(items)