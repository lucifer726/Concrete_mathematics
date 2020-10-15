# 1.	输入a 输出a的素因子分解式
import math

n = int(input("请输入："))

# list中保存素因子
list = []
# 找到小于n的所有素数
for i in range(2, n):
    for num in range(2, int(math.sqrt(n))):
        flag = 0
    if i % num == 0:
        flag = 1
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
sum = sum(count)
c = 1
for i in range(len(newlist)):
    for j in range(1, count[i] + 1):
        if c < sum:
            print(newlist[i], end='*')
            c += 1
        else:
            print(newlist[i])
