# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(curr,csum):
            if not curr:
                return 0
            csum = csum * 10 + curr.val
            if not curr.left and not curr.right:
                return csum
            return dfs(curr.left,csum)+dfs(curr.right,csum)
        return dfs(root,0)
        