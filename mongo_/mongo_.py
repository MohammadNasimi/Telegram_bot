from pymongo import MongoClient

# اتصال به سرور پایگاه داده
client = MongoClient('mongodb://localhost:27017/')

# دسترسی به یک پایگاه داده‌ی خاص
db = client['qdatabase']

# دسترسی به یک کالکشن درون پایگاه داده
collection = db['users']

# ایجاد داکیومنت‌ها
user1 = {'name': 'SAliB', 'age': 30, 'email': 'salib@example.com'}
user2 = {'name': 'Bagher', 'age': 25, 'email': 'bagher@example.com'}

# افزودن یک داکیومنت
result = collection.insert_one(user1)
print('Inserted id:', result.inserted_id)

# افزودن چند داکیومنت
result = collection.insert_many([user2])
print('Inserted ids:', result.inserted_ids)

# یافتن یک داکیومنت
result = collection.find_one({'name': 'SALiB'})
print('Found document:', result)

# دریافت تمام داکیومنت‌ها
results = collection.find()
print('All documents:')
for document in results:
    print(document)
    
# به‌روزرسانی یک داکیومنت
collection.update_one({'name': 'SALiB'}, {'$set': {'age': 35}})

# به‌روزرسانی چند داکیومنت
collection.update_many({"age": {"$lt": 18}}, {"$set": {"status": "Inactive"}})

# حذف یک داکیومنت
collection.delete_one({'name': 'Bagher'})

# حذف چند داکیومنت
collection.delete_many({"age": {"$gt": 30}})

# aggregate
results = collection.aggregate([{"$match": {"age": {"$gt": 25}}}])
for document in results:
    print(document)
    
results = collection.aggregate([{"$group": {"_id": "$age", "count": {"$sum": 1}}}])
for document in results:
    print(document)
    
results = collection.aggregate([{"$limit": 5}])
for document in results:
    print(document)
    
results = collection.aggregate([{"$sort": {"age": -1}},{"$limit": 5}])
for document in results:
    print(document)