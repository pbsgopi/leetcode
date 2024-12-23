class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        ans = 0
        while q:
            a = []
            for _ in range(len(q)):
                node = q.popleft()
                a.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            n = len(a)
            a = sorted(range(n), key = lambda i: a[i])

            vis = [False] * n
            ans += n
            for v in a:
                if vis[v]:
                    continue
                while not vis[v]:
                    vis[v] = True
                    v = a[v]
                ans -= 1
        return ans