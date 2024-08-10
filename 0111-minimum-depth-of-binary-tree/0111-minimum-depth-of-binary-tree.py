class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            right=dfs(root.right)
            left=dfs(root.left)
            if not root.left and not root.right:
                return 1
            elif not root.right:
                return left+1
            elif not root.left:
                return right+1
            else:
                return min(left,right)+1
        return dfs(root)