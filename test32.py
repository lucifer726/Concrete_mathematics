class Solution:
    def gcd(self, a: int, b: int):
        """
        输入a，b, 输出a，b的最大公约数
        :param a: 第一个数
        :param b: 第二个数
        :return:
        """
        if b == 0:
            return a
        return self.gcd(b, a % b)


if __name__ == '__main__':
    # 输入一个整数集合，输出其最大公约数
    test = Solution()
    list = [100, 80, 60, 200]
    num = list[0]
    for i in range(len(list)-1):
        num = test.gcd(num, list[i+1])
    print(num)
