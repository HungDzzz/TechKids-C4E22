person = {
    'name': 'Hung',
    'age': 22,
}
key = input("Ban muon xoa hay cap nhat ( D or U )")
while True:
    if key == 'D':
        key1 = input("Nhap key muon xoa : ")
        del person[key1]
        print(person)
        break
    if key == 'U':
        key2 = input("Nhap key muon cap nhat & value moi: ")
        pair = key2.split(",")
        key3,value = pair
        if key3 in person:
            person[key3]=value
            print(person)
            break
        else:
            print("not found")