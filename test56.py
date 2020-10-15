list = [1, 2]
# 生成小于n的fib数列
def fib(n):
    i = 2
    while list[-1] < n:
        list.append(list[i - 2] + list[i - 1])
        i += 1
    return list[:-1]

n = int(input("请输入："))
fib1 = fib(n)
fib1.reverse()      # 列表倒置
res = []
# 依次相减，如果大于0，该项为1，否则为0
for i in range(len(fib1)):
    if n < 0: break
    if n - fib1[i] >= 0:
        res.append(1)
        n = n - fib1[i]
    else:
        res.append(0)

res = [str(i)for i in res]
print(''.join(res))
