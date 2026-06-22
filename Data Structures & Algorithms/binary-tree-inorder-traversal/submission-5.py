# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def inorder(root):
            answer = []

            if not root:
                return answer
            answer += inorder(root.left)
            answer.append(root.val)
            answer += inorder(root.right)
            return answer
        return inorder(root)