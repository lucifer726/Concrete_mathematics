def baseNeg2(N):
    """
    :type N: int
    :rtype: str
    """
    if N == 0: return '0'

    b = N
    arr = []
    # 被除数 除以 -2 如果"余"为负数的情况则需要重新计算"商"值
    while b != 0:
        c = b % -2
        if c < 0:
            c = 1
            b = (b - c) // -2
        else:
            b = b // -2
        arr.append(str(c))
    arr.reverse()
    return ''.join(arr)

print(baseNeg2(2))
print(baseNeg2(3))
print(baseNeg2(100))
