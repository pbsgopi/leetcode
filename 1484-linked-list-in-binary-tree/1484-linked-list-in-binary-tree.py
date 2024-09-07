# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def subpath(root, head):
            if head is None:
                return True
            if root is None:
                return False

            if root.val != head.val:
                return False

            return subpath(root.left, head.next) or subpath(root.right, head.next)              


        def dfs(root):
            if root is None:
                return False
            
            if subpath(root, head):
                return True
            
            return dfs(root.left) or dfs(root.right)
        

        return dfs(root)