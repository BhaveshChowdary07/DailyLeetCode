class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = 0
        r = 0
        merged = []
        while(l<len(nums1) and r<len(nums2)):
            if nums1[l]<nums2[r]:
                merged.append(nums1[l])
                l+=1
            else:
                merged.append(nums2[r])
                r += 1
        while(l<len(nums1)):
            merged.append(nums1[l])
            l+=1
        while(r<len(nums2)):
            merged.append(nums2[r])
            r+=1
        n = len(merged)
        if n == 0:
            return 0
        if n%2 == 0:
            return (merged[(n//2)]+merged[(n//2)-1])/2.0
        elif n%2 == 1:
            return (merged[n/2])
                
        