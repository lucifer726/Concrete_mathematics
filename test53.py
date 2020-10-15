#  3.	1000以内，能被7整除的正整数个数 输入a，b 输出a以内，能被b整除的正整数的个数是多少个
def div(a,b):
    count = 0
    for i in range(b, a):
        if i % b == 0:
            count += 1
    return count
print(div(1000,7))
