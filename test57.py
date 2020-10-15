# 7.	输入正整数数字n，求其康托尔表示
list = [1, 2]
# 生成小于n的三元式的数列
def jc(n):
    sum,i = 2,2
    while sum < n:
        i = i+1
        sum *=i
        list.append(sum)
    return list[:-1]

n = int(input("请输入："))
jc1 = jc(n)
jc1.reverse()      # 列表倒置
res = []
# 依次相除，如果大于0，该项为商，n变为余数，否则为0
for i in range(len(jc1)):
    if n < 0: break
    if n // jc1[i] >= 0:
        res.append(n // jc1[i])
        n = n %jc1[i]
    else:
        res.append(0)

res = [str(i)for i in res]
print(''.join(res))
