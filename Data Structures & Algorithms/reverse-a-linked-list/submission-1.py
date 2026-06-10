# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        previous = None
        current = head
        nnext = current.next

        while nnext:
            current.next = previous
            previous = current
            current = nnext
            nnext = current.next
        current.next = previous
        return current    
