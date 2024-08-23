from collections import defaultdict, deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # Create the adjacency list for the graph
        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        # Initialize a color map to keep track of the color assigned to each node
        color = {}

        # Iterate over all nodes
        for node in range(1, n + 1):
            if node not in color:
                # Start BFS to color the graph
                queue = deque([node])
                color[node] = 0  # Assign an initial color
                
                while queue:
                    current = queue.popleft()
                    
                    # Check all adjacent nodes
                    for neighbor in graph[current]:
                        if neighbor not in color:
                            # Assign the opposite color to the neighbor
                            color[neighbor] = 1 - color[current]
                            queue.append(neighbor)
                        elif color[neighbor] == color[current]:
                            # If a neighbor has the same color, bipartition is not possible
                            return False
        
        # If we have successfully colored the graph, bipartition is possible
        return True