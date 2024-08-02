class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1], [1]
        res = 1
        for i in range(len(nums)-1):
            res *= nums[i]
            left.append(res)
        res = 1
        for i in range(len(nums) -1, 0, -1):
            res *= nums[i]
            right.append(res)
        right = right[::-1]

        for i in range(len(nums)):
            nums[i] = right[i] * left[i]
        return nums