class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        m = {}
        for j in range(len(nums)):
            if nums[j] in m:
                res += m[nums[j]]
            else:
                m[nums[j]] = 0
            m[nums[j]] += 1

        return res
        