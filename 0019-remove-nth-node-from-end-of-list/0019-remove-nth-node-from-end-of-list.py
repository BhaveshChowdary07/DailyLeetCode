# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # curr = head
        # prev = None
        # while(curr!=None):
        #     next_temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next_temp
        # count = 0
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        for i in range(n+1):
            fast = fast.next
        
        while fast!=None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next

        