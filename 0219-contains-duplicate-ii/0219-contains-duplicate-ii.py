class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        if k == 0:
            return 
        if len(set(nums)) == len(nums):
            return False           
        i, j = 0, 0 
        N = len(nums)
        s = set()
        while j < k:
            if nums[j] in s:
                return True
            s.add(nums[j])
            j+=1
        while j < N:
            if nums[j] in s: 
                return True
            s.remove(nums[i])
            s.add(nums[j])
            i+=1
            j+=1
        return False