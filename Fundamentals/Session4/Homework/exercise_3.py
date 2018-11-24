quiz = {
    'title': "Answer the following algebra question :",
    'question': "If x = 8, then what is the value of 4(x + 3) ?",
    'choice': ['1. 35','2. 36','3. 40','4. 44'],
    'right': 4
}
while True :
    print(quiz['title'])
    print(quiz['question'])
    for k in quiz['choice']:
        print(k)
    x = input("Your choice : ")
    if x.isdigit():
        a = int(x)
        if a == quiz['right']:
            print("Bingo")
            break
        else :
            print(":(")
    # else :
    #     print("You must enter the number")