# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if len(pairs) == 0:
            return pairs
        
        res = []
        res.append(list(pairs))
        
        def find_insertion(pairs, r, target):
            l = 0
            while l <= r:
                m = (l + r) // 2
                if pairs[m].key > target:
                    r = m - 1
                else:
                    l = m + 1
            return l

        for i in range(1, len(pairs)):

            current = pairs[i]
            new_index = find_insertion(pairs, i - 1, current.key)

            # shift elements to the right
            j = i
            while j > new_index:
                pairs[j] = pairs[j - 1]
                j -= 1
            
            pairs[new_index] = current

            res.append(list(pairs))  

        return res 
            
