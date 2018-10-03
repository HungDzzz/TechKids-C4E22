items = ['T-Shirt','Sweater']
want = input("What do you want (C, R, U, D) ? ")
if want == 'R' :
    print("Our items : ",items)
if want == 'C':
    new_items = input("Nhap vao mat hang : ")
    items.append(new_items)
    print("Our items : ",items)
if want == 'U':
    update = int(input("Update position ? "))
    new = input("New item ?")
    items[update-1] = new
    print("Our items : ",items)
if want == 'D':
    delete = int(input("Delete position ? "))
    items.pop(delete-1)
    print("Our items : ",items)


