n = int(input("enter a number ? "))
factorial = 1
for i in range(n):
    factorial = factorial * (i + 1)
n = str(n)
print(n + "! = ",factorial)