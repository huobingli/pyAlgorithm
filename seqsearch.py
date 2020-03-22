def seq_search(items, key):
    """顺序查找"""
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1

def main():
    item=[5,9,1,3,4,7,6,8,2]
    print(item)
    item = seq_search(item, 4)
    print(item)


if __name__ == '__main__':
    main()