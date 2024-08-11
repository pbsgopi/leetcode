class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack, minVal = [], float('inf')

        for n in nums:
            while stack and stack[-1][0] <= n:
                stack.pop()

            if stack and stack[-1][1] < n:
                return True
            
            minVal = min(minVal, n)
            stack.append([n, minVal])
        
        return False