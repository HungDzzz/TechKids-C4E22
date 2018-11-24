
#person_list.append(p1)
#person_list.append(p2)
#person_list = [p1,p2]
person_list = [
    {
    'name':'Hung',
    'age': 22
    },
    {
    'name': 'Hoa',
    'age': 22
    }
]
# print(person_list)
# #print(person_list[1])
# person_list[0]={
#     'name': 'HDZ',
#     'age': 22
# }
# print(person_list)
# person_list.pop(0)
print(person_list)
#p= person_list[0]
for p in person_list:
    #print(person_list[0]['age'])
    print(p['name'],p['age'],sep=" : ")