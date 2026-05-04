class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        m = {}

        for num in nums:
            if num not in m:
                m[num] = 1
            else:
                res += m[num]
                m[num] += 1

        return res
        