total = ''
for i in range(9):
    if i % 2 == 0 :
        i = 'x '
    else:
        i = '* '
    total += i
print(total)