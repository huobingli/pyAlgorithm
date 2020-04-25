import pymongo

from bson.objectid import ObjectId

# mongo 连接

def main():
    # 第一个参数为地址 host，第二个参数为端口 port（如果不给它传递参数，则默认是 27017）
    client = pymongo.MongoClient(host='47.114.171.118', port=27017)

    # 指定数据库
    db = client.test
    # db = client['test'] 意义同上

    # 指定操作集合 (集合 类似mysql的表)
    collection = db.students
    # collection = db['students'] 意义同上

    # 输出个数
    count = collection.find().count()
    print(count)

    # 输出条件个数
    count = collection.find({'age': 20}).count()
    print(count)

    # 排序 pymongo.DESCENDING 降序  pymongo.ASCENDING 升序
    results = collection.find().sort('name', pymongo.ASCENDING)
    print([result['name'] for result in results])
    
    # 偏移 skip
    results = collection.find().sort('name', pymongo.ASCENDING).skip(2)
    print([result['name'] for result in results])

    # 限制个数
    results = collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(10)
    print([result['name'] for result in results])

if __name__ == '__main__':
    main()