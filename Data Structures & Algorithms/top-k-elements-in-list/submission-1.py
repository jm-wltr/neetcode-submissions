# O(n) space
# O(n) time
# k <= n

# Edge cases:
#   single element
#   all elements are the same
#   all elements distinct (and k = n)
#   k equals number of distinct elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # Make map (number -> frequency)
        m = {}
        for num in nums:
            m[num] = m.get(num, 0) + 1

        # Put nums into n buckets representing frequency
        buckets = [[] for i in range(n + 1)]
        for (num, freq) in m.items():
            buckets[freq].append(num)
        
        # Traverse buckets to build result list
        res = []
        for freq in range(n, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
            
        