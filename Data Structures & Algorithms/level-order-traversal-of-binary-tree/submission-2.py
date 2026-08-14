from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        result = []
        while len(queue):
            iteration = []
            for i in range(len(queue)):
                current = queue.popleft()
                if current:
                    iteration.append(current.val)
                    queue.append(current.left)
                    queue.append(current.right)
            result.append(iteration)
        return result[:-1]