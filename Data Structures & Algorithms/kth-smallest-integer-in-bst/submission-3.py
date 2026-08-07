# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        answer = []
        def result(root):
            if not root:
                return
            result(root.left)
            answer.append(root.val)
            result(root.right)
        result(root)
        return answer[k-1]
        