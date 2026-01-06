class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findFirst():
            l = 0
            r = len(nums)-1
            index = -1
            while l<=r:
                m = (l+r)//2
                if nums[m]>=target:
                    r = m-1
                else:
                    l =  m+1
                if nums[m]==target:
                    index = m
            return index
        def findLast():
            l = 0
            r = len(nums)-1
            index = -1
            while l<=r:
                m = (l+r)//2
                if nums[m]<=target:
                    l =  m+1
                else:
                    r = m-1
                if nums[m]==target:
                    index = m
            return index
        return [findFirst(),findLast()]