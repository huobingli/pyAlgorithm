import pymongo

from bson.objectid import ObjectId

# mongo 查询

def main():
    client = pymongo.MongoClient(host='47.114.171.118', port=27017)
    db = client.test
    collection = db.students

    # 根据正则匹配式
    results = collection.find({'name': {'$regex': '^D.*'}})

    # 输出
    print(results)
    for result in results:
        print(result)
    
    return

    # type(result) 为字典 result 中多了一个'_id'项，是mongo插入过程中自动添加的
    result = collection.find_one({'name': 'Jordan'})
    print(type(result))
    print(result)

    # 通过'_id'查找对应对象 不存在返回None
    result = collection.find_one({'_id': ObjectId('5ea42a423387444c6680695f')})
    print(result)

    # 查找年龄为20的
    # results = collection.find({'age': 20})

    # 根据符号条件查找
    # $lt 小于
    # $gt 大于
    # $lte 小于等于
    # $gte 大于等于
    # $ne 不等于
    # $in 范围里
    # $nin 不再范围里
    # results = collection.find({'age': {'$gt': 20}})

    # 根据正则匹配式
    results = collection.find({'name': {'$regex': '^J.*'}})

    # 输出
    print(results)
    for result in results:
        print(result)

    # 区分大小写
    count = collection.find({'name': "Jordan"}).count()
    condition = {'name':'jordan'}
    count = collection.find(condition).count()
    print(count)
        

if __name__ == '__main__':
    main()