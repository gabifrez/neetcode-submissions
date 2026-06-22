# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root):
            answer = []
            if not root:
                return answer
            answer += dfs(root.left)
            answer.append(root.val)
            answer += dfs(root.right)
            return answer
        return dfs(root)[k-1]