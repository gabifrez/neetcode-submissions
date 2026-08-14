# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        result = []
        if root:
            queue.append(root)
        while len(queue):
            index = 1
            n = len(queue)
            for i in range(len(queue)):                
                current = queue.popleft()
                if index == n:
                    result.append(current.val)
                index += 1
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        return result