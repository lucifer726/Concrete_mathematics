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
    test = Solution()
    print(test.gcd(987654321, 123456789))
