# 求大于某数的最小素数
import math


def fun(x):
    # 定义素数列表
    list = [2]
    a = x
    # 求根号a，素数表中的最大数不超过根号a
    d = int(math.sqrt(a))
    i = 2
    # 循环3到a，依次除以素数表中元素，将得到的素数保存到list中
    while True:
        i += 1
        flag1 = 0
        for j in list:
            if i % j == 0:
                flag1 = 1
                break
        if flag1 == 0:
            if i > a:
                print("大于{}的最小素数为：{}".format(a, i))
                break
            if (len(list) <= d):
                list.append(i)


if __name__ == "__main__":
    fun(100000)
