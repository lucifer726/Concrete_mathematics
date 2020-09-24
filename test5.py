# 输入a，n（ n<10^5 )
# 输出n以内的、跨度为a的素数等差数列
# 如没有，则输出无符合的数列
import math
# 创建素数列表list1
a = int(input("input a:"))
n = int(input("input n:"))
list1 = list()
for i in range(2, n):
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            break
    else:
        list1.append(i)
# 寻找跨度为a的等差数列初始值
new_list = list()
for i in range(1, len(list1)):
    if list1[i] + a in list1 and list1[i] + a * 2 in list1:
        key = list1[i]
        break
    else:
        print("无符合的数列")
# 将该数列添加到new_list中
for j in range(len(list1)):
    if key + j * a in list1:
        new_list.append(key + j * a)
    if key + (j + 1) * a not in list1:
        break
print(new_list)
