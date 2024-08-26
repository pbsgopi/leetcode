class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res=[]
        def dfs(root,res):
            if not root:
                return
            for x in root.children:
                dfs(x,res)
            res.append(root.val)
        dfs(root,res)
        return res