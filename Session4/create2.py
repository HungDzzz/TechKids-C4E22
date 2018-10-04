person = {
    "name": "Hung",
    "age": 22,
}
new_item = input("Nhap key & value : ")
pair = new_item.split(",")
#key=pair[0]
#value=pair[1]
#new_value = input("Nhap value : ")
key,value = pair
person[key]= value
print(person)