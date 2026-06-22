# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        answer = []
        if root:
            queue.append(root)
        while len(queue):
            counter = 0
            length = len(queue)
            for i in range(length):
                counter += 1
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                if counter == length:
                    answer.append(current.val)
        return answer
