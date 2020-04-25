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

    

if __name__ == '__main__':
    main()