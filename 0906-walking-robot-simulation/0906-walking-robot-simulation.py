class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set((a, b) for a, b in obstacles)
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        d = 0
        res = 0
        x, y = 0, 0
        for num in commands:
            if num == -2:
                d -= 1
                d += 4
                d %= 4
            
            elif num == -1:
                d += 1
                d %= 4
                
            else:
                dx, dy = dirs[d]
                for k in range(1, num+1):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in obstacles:
                        break
                    x, y = nx, ny
            res = max(res, x*x + y*y)
        return res