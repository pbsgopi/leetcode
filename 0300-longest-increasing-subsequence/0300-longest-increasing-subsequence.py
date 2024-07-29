class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:

        arr = [nums.pop(0)]                  # <-- 1) initial step
 
        for n in nums:                       # <-- 2) iterate through nums
            
            if n > arr[-1]:
                arr.append(n)

            else:
                arr[bisect_left(arr, n)] = n 

        return len(arr)