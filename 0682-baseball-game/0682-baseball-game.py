class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        for i in operations:
            if i == '+':
                if len(stack)>=2:
                    score = stack[-1]+stack[-2]
                    stack.append(score)
            elif i == 'D':
                if len(stack)>=1:
                    score = stack[-1]*2
                    stack.append(score)
            elif i == 'C':
                if len(stack)>=1:
                    stack.pop()
            else:
                stack.append(int(i))
        return sum(stack)
            