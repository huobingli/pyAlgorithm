import pymongo

from bson.objectid import ObjectId

# mongo 修改

def main():
    client = pymongo.MongoClient(host='47.114.171.118', port=27017)
    db = client.test
    collection = db.students

    
    condition = {'name': 'Jordan'}
    student = collection.find_one(condition)
    student['age'] = 25

    # 执行结果 {'n': 1, 'nModified': 1, 'ok': 1.0, 'updatedExisting': True}
    # ok 代表执行成功，nModified 代表影响的数据条数。
    result = collection.update(condition, student)
    print(result)

    result = collection.update(condition, {'$set': student})
    print(result)

    # update 官方不推荐使用 
    # 推荐使用update_one update_many 用法更加严格
    condition = {'name': 'Mike'}
    student = collection.find_one(condition)
    student['age'] = 31
    result = collection.update_one(condition, {'$set': student})
    print(result)
    print(result.matched_count, result.modified_count)

    # $inc => age += 11
    condition = {'age': {'$gt': 30}}
    result = collection.update_one(condition, {'$inc': {'age': 11}})
    print(result)
    print(result.matched_count, result.modified_count)

    condition = {'age': {'$in': [25,26]}}
    result = collection.update_many(condition, {'$inc': {'age': 1}})
    print(result)
    print(result.matched_count, result.modified_count)

if __name__ == '__main__':
    main()