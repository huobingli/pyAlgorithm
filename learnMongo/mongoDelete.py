import pymongo

from bson.objectid import ObjectId

# mongo 删除

def main():
    client = pymongo.MongoClient(host='47.114.171.118', port=27017)
    db = client.test
    collection = db.students

    # 删除所有 name 为Kevin
    result = collection.remove({'name': 'Kevin'})
    print(result)

    # 删除一条 name 为Kevin
    result = collection.delete_one({'name': 'Kevin'})
    print(result)
    print(result.deleted_count)

    # 删除age 大于40的
    result = collection.delete_many({'age': {'$gt': 40}})
    print(result.deleted_count)

if __name__ == '__main__':
    main()