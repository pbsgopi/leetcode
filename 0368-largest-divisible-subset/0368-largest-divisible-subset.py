class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort() 
        cache = {}
        def helper(i, prev):
            if i == len(nums):
                return []
            if (i, prev) in cache: return cache[(i, prev)]
            skipped = helper(i + 1, prev)
            if nums[i] % prev == 0:
                included = [nums[i]] + helper(i + 1, nums[i])
                if len(skipped) > len(included): 
                    cache[(i, prev)] = skipped
                    return cache[(i, prev)]
                else:
                    cache[(i, prev)] = included
                    return cache[(i, prev)]
            return skipped
        return helper(0, 1)
# Test the solution
solution = Solution()
nums = [1, 2, 3, 4]
print(solution.largestDivisibleSubset(nums))
