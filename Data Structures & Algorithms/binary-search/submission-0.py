class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1

        while i <= j:  # Fixing loop condition
            mid = (i + j) // 2  # Fixing integer division

            if nums[mid] == target:
                return mid  # Return correct index
            elif nums[mid] > target:
                j = mid - 1  # Move left
            else:
                i = mid + 1  # Move right

        return -1
                

        