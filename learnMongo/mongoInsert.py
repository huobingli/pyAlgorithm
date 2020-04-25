import pymongo

from bson.objectid import ObjectId

# mongo 增加

def main():
    client = pymongo.MongoClient(host='47.114.171.118', port=27017)
    db = client.test
    collection = db.students

    # 插入一条数据
    student = {
        'id': '20170101',
        'name': 'Kevin',
        'age': 20,
        'gender': 'male'
    }

    # 每条数据其实都有一个 _id 属性来唯一标识。
    # 如果没有显式指明该属性，MongoDB 会自动产生一个 ObjectId 类型的 _id 属性。
    # insert() 方法会在执行后返回_id 值。 
    result = collection.insert(student)
    print(result) 

    # 插入多条数据
    student1 = {
        'id': '20170101',
        'name': 'Jordan',
        'age': 20,
        'gender': 'male'
    }

    student2 = {
        'id': '20170202',
        'name': 'Mike',
        'age': 20,
        'gender': 'male'
    }

    # 这里用列表方式传入
    # 返回结果也是列表方式
    result = collection.insert([student1, student2])
    print(result)

    # pymongo 官方不推荐使用insert
    # 推荐使用 insert_one 和 insert_many 插入一条或者多条记录
    student = {
        'id': '20170101',
        'name': 'Jordan',
        'age': 20,
        'gender': 'male'
    }

    result = collection.insert_one(student)
    print(result)
    print(result.inserted_id)

    student1 = {
        'id': '20170101',
        'name': 'Jordan',
        'age': 20,
        'gender': 'male'
    }

    student2 = {
        'id': '20170202',
        'name': 'Mike',
        'age': 20,
        'gender': 'male'
    }

    result = collection.insert_many([student1, student2])
    print(result)
    print(result.inserted_ids)

    
if __name__ == '__main__':
    main()