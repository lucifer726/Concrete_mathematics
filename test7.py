# 编程实现上述四个性质，快速判断一个数字是不是完全数
# 输入n，输出true/false

import math


# 性质1：除6以外，各个位数相加，直到变为个位数，结果为1
def judge1(n):
    if (n == 6):
        return True
    else:
        # 将整数转为字符串，依次相加
        sum_value = sum(int(i) for i in str(n))
        # 如果值大于等于10，继续依次相加
        while sum_value >= 10:
            sum_value = sum(int(i) for i in str(sum_value))
        if (sum_value == 1):
            return True
        else:
            return False


# 性质2：可以表达为2的连续正整数次幂之和
def judge2(n):
    flag = False
    count = 0
    for i in range(1, 100):
        if (2 ** i > n):
            return False
        sum = 0
        for j in range(i, 100):
            sum += 2 ** j
            count += 1
            if (sum == n):
                flag = True
                break
            if (sum > n):
                break
        count = 0
        if (flag):
            break
    if (isPrime(count)):
        return True
    else:
        return False


def isPrime(n):
    flag = True
    for mod in range(2, int(math.sqrt(n)) + 1):
        if (n % mod == 0):
            flag = False
            break
    return flag


# 性质3：所有完全数都是三角形数
def judge3(n):
    sum, i = 0, 1
    while sum < n:
        sum += i
        i += 1
        if (sum == n):
            return True
    return False


# 性质4：除6以外的完全数，都可以表示为连续奇立方之和
def judge4(n):
    if (n == 6):
        return True
    else:
        sum, i = 0, 1
        while sum < n:
            sum += i ** 3
            i += 2
            if (sum == n):
                return True
        return False


def isPerfectNum(n):
    a = 1
    b = n
    sum = 0
    # 如果a>b,则说明因子已全部找完
    while a < b:
        if n % a == 0:
            # 如果能够整除，就将因子相加
            sum += (a + b)
        a += 1
        b = n / a
    if (a == b) and (n % a == 0):
        sum += a
    return (sum - n) == n


if __name__ == '__main__':
    num = int(input("输入一个数:"))
    if (judge1(num) and judge2(num) and judge3(num) and judge4(num)):
        if (isPerfectNum(num)):
            print("完全数")
    else:
        print("不是完全数")
