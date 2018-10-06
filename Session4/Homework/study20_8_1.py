a = input("Nhap chuoi can kiem tra : ")
letter_counts = {}
for letter in a:
    if letter.isupper() :
        letter = letter.lower()
    if not letter.isspace() :
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
letter_items = list(letter_counts.items())
letter_items.sort()
#print(letter_items)
for k,v in letter_items:
    print(k,v,sep='   ')