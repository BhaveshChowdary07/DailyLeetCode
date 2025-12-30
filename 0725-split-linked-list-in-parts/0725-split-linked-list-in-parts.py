# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: List[Optional[ListNode]]
        """
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length+=1
        base_len = length // k
        remainder = length % k
        
        curr = head
        res = []
        for i in range(k):
            res.append(curr)
            for j in range(base_len-1+(1 if remainder else 0)):
                if not curr: break
                curr = curr.next
            remainder -= (1 if remainder else 0)
            if curr:
                curr.next,curr = None,curr.next
        return res