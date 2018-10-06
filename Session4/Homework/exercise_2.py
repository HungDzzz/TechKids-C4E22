prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
for k in prices.keys():
    print(k)
    print("prices :",prices[k])
    print("stock :",stock[k])
    print()
total = 0
for k in prices.keys() :
    print("So tien kiem duoc tu",k,"la :",(prices[k]*stock[k]))
    total += prices[k]*stock[k]
print("Tong so tien kiem duoc khi ban tat ca do an la :",total)