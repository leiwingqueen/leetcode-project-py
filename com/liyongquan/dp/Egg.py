"""
https://leetcode-cn.com/problems/super-egg-drop/
经典算法题
"""


# searchTime(K, N) = max(searchTime(K - 1, X - 1), searchTime(K, N - X))+1
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        if N == 0 or K == 1 or N == 1:
            return N
        min1 = N
        for x in range(1, N+1):
            result = max(self.superEggDrop(K - 1, x-1), self.superEggDrop(K, N - x))+1
            if result < N:
                min1 = result
        print('计算结果...k:{0},n:{1},result:{2}'.format(K, N, min1))
        return min1


so = Solution()
r = so.superEggDrop(2, 6)
print(r)
