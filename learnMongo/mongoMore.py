import pymongo

from bson.objectid import ObjectId

# mongo 连接

def main():
    client = pymongo.MongoClient(host='47.114.171.118', port=27017)
    db = client.test
    collection = db.students

    # 找到删除
    result = collection.find_one_and_delete({'name': 'Kevin'})
    print(result)

    # 找到替换
    result = collection.find_one_and_replace({'name': 'Kevin'}, {'name': 'Durant'})
    print(result)
    
    # 找到更新
    result = collection.find_one_and_update({'name': 'Durant'}, {"$inc":{"age":1}})
    print(result)
    

if __name__ == '__main__':
    main()