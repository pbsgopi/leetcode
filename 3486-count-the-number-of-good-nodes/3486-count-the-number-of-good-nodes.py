class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        tree = defaultdict(list)
        for i, j in edges:
            tree[i].append(j)
            tree[j].append(i)      
        def dfs(node, parent):
            s = 1
            childs = []
            for i in tree[node]:
                if i == parent:
                    continue
                size = dfs(i, node)
                s += size
                childs.append(size)
            if len(set(childs)) <= 1:
                self.good_nodes += 1
            return s
        self.good_nodes = 0
        dfs(0, -1)
        return self.good_nodes