class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)
        print(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) == 0:
            self.nums.append(val)
            return self.nums[self.k - 1]
        l = 0
        r = len(self.nums) - 1
        mid = 0
        while l < r:
            print(l, r)
            mid = l + (r - l) // 2
            if val < self.nums[mid]:
                l = mid + 1
            elif val > self.nums[mid]:
                r = mid
            else:
                break
        if val < self.nums[mid]:
            self.nums.insert(mid + 1, val)
        else:
            self.nums.insert(mid, val)
        return self.nums[self.k - 1]