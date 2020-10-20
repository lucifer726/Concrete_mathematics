# 输入n，输出分子分母都不大于n的有序最简分数序列
from fractions import Fraction

n = int(input("请输入n ："))

listkey, listvalue = [], []
# 找到分子分母都都不大于n的所有数
for i in range(1, n + 1):
    for j in range(1, n + 1):
        a = Fraction(i, j)          # Fraction函数可以表示分数
        listkey.append(str(a))      # 将分数的表示添加到key中
        listvalue.append(i / j)     # 将分数对应的值添加到value中

# 将俩个列表合并成一个字典
mydict = dict(zip(listkey, listvalue))
# 按照values对字典进行排序
d2 = dict(sorted(mydict.items(),key=lambda x:x[1]))
# 以逗号分隔，输出key
print(','.join(map(str, d2.keys())))
