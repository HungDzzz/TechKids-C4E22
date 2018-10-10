from matplotlib import pyplot
from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_default_database()
customer = db["customers"]
customers = customer.find()
reference = {
   "events": 0,
   "wom": 0,
   "ads": 0
}
for i in customers:
    if i["ref"] == "events":
        reference["events"]+=1
    elif i["ref"] == "wom":
        reference["wom"]+=1
    elif i["ref"] == "ads":
        reference["ads"]+=1
print(reference)
# 1. Prepare data
reference_counts = [reference['events'], reference['wom'], reference['ads']]
# 2. Prepare labels
reference_name = ['events', 'wom', 'ads']
# 3. Draw pie
pyplot.pie(reference_counts, labels=reference_name, autopct="%.1f%%", shadow=True, explode=[0, 0, 0.1])
pyplot.title("Events vs Wom vs Ads")
pyplot.axis("equal")
# 4. Show
pyplot.show()
