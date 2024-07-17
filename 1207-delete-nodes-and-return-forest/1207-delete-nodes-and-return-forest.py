# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        ans = []
        to_delete = set(to_delete)
        
        def helper(node):
            if not node:
                return None
            node.left = helper(node.left)
            node.right = helper(node.right)
			
			# add children of a node that is to be deleted
            if node.val in to_delete:
                if node.left: 
                    ans.append(node.left)
                if node.right:
                    ans.append(node.right)
                return None
            return node
                
        helper(root)
		# if root is not to be deleted then add it
        if root.val not in to_delete:
            ans.append(root)
        return ans
                