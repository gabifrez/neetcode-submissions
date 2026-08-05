# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(root):
            if not root:
                return root
            if key > root.val:
                root.right = delete(root.right)
            elif key < root.val:
                root.left = delete(root.left)
            else:
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                cur = root.right
                while cur.left:
                    cur = cur.left
                cur.left = root.left
                res = root.right
                del root
                return res
            return root
        return delete(root)

        