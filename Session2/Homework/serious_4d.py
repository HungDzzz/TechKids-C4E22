n = int(input("nhap n : "))
total = ''
for i in range(n):
    if i % 2 == 0 :
        i = 'x '
    else:
        i = '* '
    total += i
print(total)