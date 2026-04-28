class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = {}
        for i in range(len(nums)):
           difference[nums[i]] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in difference and difference[diff] !=i:
                return [i,difference[diff]]
        