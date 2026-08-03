# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        current = head
        nnext = head.next
        while nnext !=slow:
            current.next = prev
            prev = current
            current = nnext
            nnext = nnext.next
        current.next = prev
        
        maxim = 0
        while current:
            maxim = max(maxim, current.val + slow.val)
            current = current.next
            slow = slow.next
        return maxim
        