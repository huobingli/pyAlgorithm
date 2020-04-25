import pymongo

from bson.objectid import ObjectId

# mongo 连接

def main():
    client = pymongo.MongoClient(host='47.114.171.118', port=27017)
    db = client.test
    collection = db.students

    # 删除数据
    result = collection.remove()
    print(result)
    count = collection.count()
    print(count)

    # 删除表
    result = collection.drop()
    print(result)
    count = collection.count()
    print(count)


if __name__ == '__main__':
    main()