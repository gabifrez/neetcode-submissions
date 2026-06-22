# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def bfs(root):
            queue = deque()
            answer = []
            if root:
                queue.append(root)
            while len(queue) > 0:
                level = []
                for i in range(len(queue)):
                    current = queue.popleft()
                    level.append(current.val)
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)
                answer.append(level)
            return answer
        return bfs(root)
