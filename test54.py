# 4.	输入n，将其表示为连续正整数的和的形式


def addSeq(n):
    # 定义两个指针，分别为1，2
    start, end = 1, 2
    # 定义结束点为n的一半
    stop = (n + 1) / 2
    # mysum为start和end的和
    mysum = start + end
    p = []
    while start < stop:
        # 如果等于21，打印start到end的数列，start，end全部后移
        if mysum == n:
            p.append(range(start, end+1))
            mysum -= start
            start += 1
            end += 1
            mysum += end
        # 如果小于21，end后移
        elif mysum < n:
            end += 1
            mysum += end
        #  如果sum大于21，start后移
        else:
            mysum -= start
            start += 1
    for i in p:
        print(list(i))

if __name__ == '__main__':
    addSeq(33)
