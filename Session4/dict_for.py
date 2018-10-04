person = {
    'name': 'Hung',
    'age': 22,
}
# for k in person.keys():
#     print(k,end=' ')
#     print(person[k])
# for v in person.values():
#     print(v)
#    # print(person[v])
for k,v in person.items():
    print(k,v,sep=' : ')