# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head or not head.next:
            return True
        slow = fast = head
        while(fast!=None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        curr = slow
        prev = None
        while(curr):
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        l = head
        r = prev
        while(l and r):
            if l.val!=r.val:
                return False
            l = l.next
            r = r.next
        return True

