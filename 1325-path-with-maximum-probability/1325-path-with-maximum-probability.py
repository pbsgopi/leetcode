class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj=collections.defaultdict(list)
        for i in range(len(edges)):
            src,dst=edges[i]
            adj[src].append([dst,succProb[i]])
            adj[dst].append([src,succProb[i]])
        pq=[(-1,start)]
        visit=set()
        while pq:
            prob,cur=heapq.heappop(pq)
            visit.add(cur)
            if cur==end:
                return -1*prob
            for i,j in adj[cur]:
                if i not in visit:
                    heapq.heappush(pq,(prob*j,i))
        return 0