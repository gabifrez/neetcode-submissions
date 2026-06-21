# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, answer):
        if not root:
            return answer
        self.inorder(root.left, answer)
        answer.append(root.val)
        self.inorder(root.right, answer)
        return answer


    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:


        return self.inorder(root, [])
        