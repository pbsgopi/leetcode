class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)       
        minFromLeft = [nums[0]]
        for i in range(1, n):
            minFromLeft.append(min(minFromLeft[i-1], nums[i]))
        stack = [] 
        for j in range(n-1, -1, -1):
            if nums[j] > minFromLeft[j]:
                while stack and stack[-1] <= minFromLeft[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])       
        return False