class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:  # Edge case: Empty array
            return 0

        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        total_water = 0

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                total_water += max(0, leftMax - height[left])
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                total_water += max(0, rightMax - height[right])

        return total_water

