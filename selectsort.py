def select_sort(items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items

def main():
    item=[5,9,1,3,4,7,6,8,2]
    print(item)
    item = select_sort(item)
    print(item)


if __name__ == '__main__':
    main()