# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(root, targetSum):
            if root and not root.left and not root.right:
                if targetSum == root.val: return True
            if not root: return False
            left = helper(root.left, targetSum - root.val)
            right = helper(root.right, targetSum - root.val)
            return left or right
        return helper(root, targetSum)