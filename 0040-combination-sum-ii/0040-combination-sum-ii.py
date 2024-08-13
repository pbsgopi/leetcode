class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtrack(start, target, path):
            if target == 0:
                result.append(path.copy())
                return
            if target <= 0:
                return
            prev=-1
            for i in range(start,len(candidates)):
                if candidates[i]==prev:
                    continue
                path.append(candidates[i])
                backtrack(i+1, target - candidates[i], path)
                path.pop()
                prev=candidates[i]
        backtrack(0, target, [])
        return result