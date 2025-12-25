# import math
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Dynamic programming
        if n == 1:
            return 1
        if n == 2:
            return 2
        a = [1,2]
        for i in range(2,n):
            a.append(a[i-1]+a[i-2])
        return a[-1]
    #     ways = 0
    #     for i in range(n//2 + 1):
    #         ways += self.nCr(n - i, i)
    #     return ways
    # def nCr(self,n, r):
    #     return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))