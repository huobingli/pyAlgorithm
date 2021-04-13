#闭包函数，其中 exponent 称为自由变量
def nth_power(exponent):
    def exponent_of(base):
        print("exponent_of")
        return base ** exponent
    print("nth_power")    
    return exponent_of # 返回值是 exponent_of 函数


if __name__ == '__main__':
    square = nth_power(2) # 计算一个数的平方
    cube = nth_power(3) # 计算一个数的立方
    print(square(2))  # 计算 2 的平方
    print(cube(2)) # 计算 2 的立方