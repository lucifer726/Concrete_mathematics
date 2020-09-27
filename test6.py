# 输出第四个、第五个完全数

def isPerfectNum(n):
    a = 1
    b = n
    sum = 0
    # 如果a>b,则说明因子已全部找完
    while a < b:
        if n % a == 0:
            # 如果能够整除，就将因子相加
            sum += (a + b)
        a += 1
        b = n / a
    if (a == b) and (n % a == 0):
        sum += a
    return (sum - n) == n


count, i = 0, 0
while count < 4:
    i += 1
    if isPerfectNum(i):
        count += 1
        print(i)
