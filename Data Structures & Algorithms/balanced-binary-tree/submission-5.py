class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        def solution(node):
            if not node:
                return True
            left = height(node.left)
            right = height(node.right)

            if abs(left - right) > 1:
                return False
            return solution(node.left) and solution(node.right)

        return solution(root)