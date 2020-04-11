# 斐波那契数列


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        f0 = 0
        f1 = 1
        for i in range(2, n + 1):
            temp = (f0 + f1)%1000000007
            f0 = f1
            f1 = temp
            # print(f1)
        return f1


so = Solution()
print('结果:', so.fib(45))
