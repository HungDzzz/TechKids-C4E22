items = ['com','pho','my','bun']

print(items)
items.pop(1) # xoa theo vi tri
items.remove("com") # xoa theo noi dung
print(items)
print(*items,sep=',')