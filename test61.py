# 输入一个正整数n, 求根号n的前10位连分数
import math

n = int(input("请输入n："))
n = math.sqrt(n)
# 建立列表用于存储
list = []
# 用i计数
i = 1
# x向下取整
x = math.floor(n)
m = n - x
# 存入列表
list.append(str(x))
# 循环处理
while i < 10:
    x = math.floor(1 / m)
    m = 1/m - x
    list.append(str(x))
    i += 1

print(''.join(list))
