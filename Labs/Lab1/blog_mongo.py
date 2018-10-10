from pymongo import MongoClient

uri = "mongodb://hungdz:anhhung1996@ds245022.mlab.com:45022/lab_techkids"

#connect to database
client = MongoClient(uri)
db = client.get_default_database()

#collection
posts = db['posts'] #chon thu muc
post_list = posts.find()
for p in post_list:
#p = post_list[0]
    print(p['author'])
    print(p['title'])
    print(p['content'])

# #document
# #create a document
# post = {
#     'title': 'Hello me',
#     'content': 'hom nay troi mua',
#     'author': 'me'
# }
# # insert created document
# posts.insert_one(post)
#insert_one(C) , find(R)
