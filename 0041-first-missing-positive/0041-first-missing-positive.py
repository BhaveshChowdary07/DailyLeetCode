class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            if nums[i]<0:
                nums[i]=0
        for i in range(n):
            a = abs(nums[i])
            if 1 <= a <= n:
                if nums[a-1]>0:
                    nums[a-1] *= -1
                elif nums[a-1] == 0:
                    nums[a-1] = -1*(n+1)
        for i in range(1,n+1):
            if nums[i-1]>=0:
                return i
        return n+1