quiz = []
question_1 = {
    'title': "Answer the following algebra question :",
    'question': "If x = 8, then what is the value of 4(x + 3) ?",
    'choice': ['1. 35','2. 36','3. 40','4. 44'],
    'right': 4
}
question_2 = {
    'title': "Estimate this answer ( exact calculation not needed) :",
    'question': 'Jack scored these marks in 5 math tests : 49, 81, 72, 66 and 52. What is the mean ?',
    'choice': ['1. About 55', '2. About 65', '3. About 75', '4. About 85'],
    'right': 2
}
quiz.append(question_1)
quiz.append(question_2)
count = 0
print(quiz[0]['title'])
print(quiz[0]['question'])
for k in quiz[0]['choice']:
    print(k)
x = input("Your choice : ")
if x.isdigit():
    a = int(x)
    if a == quiz[0]['right']:
        print("Bingo")
        count += 1
    else :
        print(":(")
print(quiz[1]['title'])
print(quiz[1]['question'])
for k in quiz[1]['choice']:
    print(k)
y = input("Your choice : ")
if x.isdigit():
    b = int(y)
    if b == quiz[1]['right']:
        print("Bingo")
        count += 1
    else :
        print(":(")
print("You correctly answer",count,"out of 2 questions")