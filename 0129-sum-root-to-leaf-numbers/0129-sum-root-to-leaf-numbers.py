# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def helper(root, temp):
            if not root: return
            if not root.left and not root.right:
                nonlocal ans
                ans += temp * 10 + root.val
                return 
            helper(root.left, temp * 10 + root.val)
            helper(root.right, temp * 10 + root.val)
        helper(root, 0)
        return ans