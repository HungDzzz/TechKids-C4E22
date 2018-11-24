from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_default_database()
posts = db['posts']
post = {
    'title': 'TechKids thật là một nơi tuyệt vời',
    'content': 'Các bạn C4E tiếp theo! Chúc các bạn học được nhiều điều bổ ích',
    'author': 'Hoàng Quang Hùng'
}
posts.insert_one(post)