# 8.	输入非零整数数字n，求其平衡三元展开
list = [1, 3]
# 生成小于n的三元式的数列
def sy(n):
    sum,i = 3,2
    while sum < n:
        i = i+1
        sum *=i
        list.append(sum)
    return list[:-1]

n = int(input("请输入："))
sy1 = sy(n)
sy1.reverse()      # 列表倒置
res = []
# 依次相除，如果大于0，该项为商，n变为余数，否则为0
for i in range(len(sy1)):
    if n < 0: break
    if n // sy1[i] >= 0:
        res.append(n // sy1[i])
        n = n %sy1[i]
    else:
        res.append(0)

res = [str(i)for i in res]
print(''.join(res))
