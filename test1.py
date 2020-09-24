# 输入 自然数a,b,c
# 输出 a^b mod c 的结果

# 输入a,b,c
a = int(input("input a:"))
b = int(input("input b:"))
c = int(input("input c:"))
# rem1为a对c的同余数
rem1 = a % c
# 将rem1赋值给mul
mul = rem1
# mul不断乘以rem1，且模除c小于等于1时，结束循环
count = 1
while mul % c > 1:
    mul *= rem1
    count += 1
# rem2和d，用来计算最终得数
rem2 = b % count
d = 1
for i in range(rem2):
    d *= rem1
print(d % c)
