person = {
    "name": "Hung",
    "age":22,
}
key=input("Nhap doi tuong can xem :")
#pair=key.split(",")
if key in person:
    #key1=pair[0]
    #value = pair[1]
    print(person[key])
    #print(person[value])
else:
    print("not found")