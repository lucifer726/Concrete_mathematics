# 2.	输入一个整数集合，输出其最大公约数

import math


def syz(n):
    # list中保存素因子
    list = []
    # 找到小于n的所有素数
    for i in range(2, n):
        j = 2
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            list.append(i)

    # count中保存阶数
    count = []
    newlist = []
    # 如果a能够整除对应素数，则记录阶数，添加到count中
    for i in list:
        m = 0
        if n % i == 0:
            newlist.append(i)
        while n % i == 0:
            m += 1
            n = n / i
        if m > 0:
            count.append(m)

    return newlist, count


a1, a2, b1, b2 = [], [], [], []
a1, a2 = syz(30)
b1, b2 = syz(105)
k = 1
minc3 = []
c3 = [val for val in a1 if val in b1]

for j in a1:
    for k in b1:
        if j == k:
            minc3.append(min(a2[a1.index(j)], b2[b1.index(k)]))

sum = sum(minc3)
c = 1
for i in range(len(c3)):
    for j in range(1, minc3[i] + 1):
        if c < sum:
            print(c3[i], end='*')
            c += 1
        else:
            print(c3[i])
