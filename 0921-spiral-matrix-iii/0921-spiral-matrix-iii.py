class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        total = rows * cols
        step = 1
        res = []
        while total > 0:
            for i in range(step):
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    res.append([rStart, cStart])
                    total -= 1
                cStart += 1
            for i in range(step):
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    res.append([rStart, cStart])
                    total -= 1
                rStart += 1
            step += 1
            for i in range(step):
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    res.append([rStart, cStart])
                    total -= 1
                cStart -= 1
            for i in range(step):
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    res.append([rStart, cStart])
                    total -= 1
                rStart -= 1
            step += 1
        return res