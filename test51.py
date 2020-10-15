# 1.	输入a 输出a的素因子分解式
import math

primelist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

n = int(input("请输入："))

# newlist中保存素因子
newlist = []
# 找到小于根号n的所有素数
for i in primelist:
    if i <= math.sqrt(n):
        newlist.append(i)
    else:
        break

# count中保存阶数
count = []
# 如果a能够整除对应素数，则记录阶数，添加到count中
for i in newlist:
    a = n
    m = 0
    while a % i == 0:
        m += 1
        a = a / i
    count.append(m)

for i in range(len(newlist)):
    print(newlist[i], end='*')
    if i != len(newlist) - 1:
        print(count[i], end='+')
    else:
        print(count[i])
