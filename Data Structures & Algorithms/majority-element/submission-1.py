class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        maj = 0
        c = 0
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
        for key, value in dic.items():
            if value > c:
                c = value
                maj = key     
        return maj

            
        

        