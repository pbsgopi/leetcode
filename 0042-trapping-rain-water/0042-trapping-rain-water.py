class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        stack = []
        
        for right in range(n):
            while stack and height[stack[-1]] < height[right]:
                mid = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                minHeight = min(height[right] - height[mid], height[left] - height[mid])
                width = right - left - 1
                water += minHeight * width
            stack.append(right)
        
        return water
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        stack = []
        
        for right in range(n):
            while stack and height[stack[-1]] < height[right]:
                mid = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                minHeight = min(height[right] - height[mid], height[left] - height[mid])
                width = right - left - 1
                water += minHeight * width
            stack.append(right)
        
        return water