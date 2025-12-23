class Solution(object):
    def dailyTemperatures(self, temp):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0]*len(temp)
        stack = []
        for i,t in enumerate(temp):
            while stack and t>stack[-1][0]:
                stackTemp , stackInd = stack.pop()
                res[stackInd] = (i-stackInd)
            stack.append([t,i])
        return res
