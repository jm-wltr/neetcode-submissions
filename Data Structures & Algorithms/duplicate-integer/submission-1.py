class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for i in nums:
            nums_set.add(i);
        return len(nums_set) < len(nums)
        