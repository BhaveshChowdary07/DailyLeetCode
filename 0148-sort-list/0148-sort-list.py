# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        lis = []
        while curr:
            lis.append(curr.val)
            curr = curr.next
        lis.sort()
        dummy = ListNode(0)
        node = dummy
        for i in lis:
            node.next = ListNode(i)
            node = node.next
        return dummy.next
