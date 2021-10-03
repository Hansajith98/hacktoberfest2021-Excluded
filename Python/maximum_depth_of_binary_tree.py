class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if (root is None):
            return 0
        if (root.left is None and root.right is None):
            return 1

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1