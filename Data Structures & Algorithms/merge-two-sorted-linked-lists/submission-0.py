# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode('')
        head = result
        while list1 and list2:
            val1 = list1.val
            val2 = list2.val
            if val1 > val2:
                result.next = list2
                list2 = list2.next
            else:
                result.next = list1
                list1 = list1.next
            result = result.next
            
        while list1 or list2:
            if list1:
                result.next = list1
                list1 = list1.next
            if list2:
                result.next = list2
                list2 = list2.next
            result = result.next

        head = head.next
        return head
