# 求 a以内的所有幸运数

# 输入a
a = int(input("input a:"))
# 先去除序号能被2整除的项
list1 = list(range(1, a + 1, 2))

j = 1
# 当序号大于列表长度，退出循环
while j < len(list1):
    # 确定需要弹出的次数
    for i in range(1, len(list1) // list1[j] + 1):
        # 将对应位置所在的值弹出
        list1.pop(i * (list1[j] - 1))
    # 选择下一个序号
    j += 1

# 输出最大值
print(list1[-1])
