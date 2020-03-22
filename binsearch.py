def bin_search(items, key):
    """折半查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1

def main():
    item=[5,9,1,3,4,7,6,8,2]
    print(item)
    item = bin_search(item, 4)
    print(item)


if __name__ == '__main__':
    main()