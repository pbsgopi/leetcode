class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap={i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            hashmap[i].append(j)
        visited=set()
        def dfs(node):
            if node in visited:
                return False
            if hashmap[node]==[]:
                return True
            visited.add(node)
            for pre in hashmap[node]:
                if not dfs(pre):
                    return False
            visited.remove(node)
            hashmap[node]=[]
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True