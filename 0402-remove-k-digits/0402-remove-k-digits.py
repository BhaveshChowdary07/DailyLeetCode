class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # res = [0]*len(temp)
        if len(num) <= k:
            return "0"
        stack = []
        for i in num:
            while k>0 and stack and stack[-1] > i:
                stack.pop()
                k-=1
            stack.append(i)
        stack = stack[:-k] if k else stack
        number = ''.join(stack).lstrip('0')
        return number if number else "0"
        


        