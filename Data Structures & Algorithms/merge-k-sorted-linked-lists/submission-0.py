# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def find_minim(self, lists):
        low_node = lists[0]
        low_index = 0
        for i in range(len(lists)):
            if low_node == None:
                low_node = lists[i]
                low_index = i
            if lists[i] and lists[i].val < low_node.val:
                low_node = lists[i]
                low_index = i
        if low_node:
            lists[low_index] = lists[low_index].next
            return low_node
        if low_node == None:
            return None



    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        head = self.find_minim(lists)
        end = head
        while end:
            end.next = self.find_minim(lists)
            end = end.next

        return head


            
        