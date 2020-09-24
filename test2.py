# 输入正整数a
# 输出a以内的素数的个数
import math
# 定义素数列表
list = [2]
a = int(input("input a:"))
print(2)
# 求根号a，素数表中的最大数不超过根号a
b = int(math.sqrt(a))
count = 1
# 循环3到a，依次除以素数表中元素，将得到的素数保存到list中
for i in range(3, a):
    flag = 0
    for j in list:
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        print(i)
        count += 1
        if(len(list)<=b):
            list.append(i)

print("{}以内素数个数为：{}".format(a, count))
