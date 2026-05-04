class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}   # value -> index
        
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            
            if diff in mapping:
                return [mapping[diff], i]
            
            mapping[num] = i
        