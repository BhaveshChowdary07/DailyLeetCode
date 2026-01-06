class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        h = len(nums)-1
        m = -1
        while(l<h):
            m = (l+h)//2
            if nums[m]>nums[m+1]:
                h = m
            else:
                l = m+1
        return l