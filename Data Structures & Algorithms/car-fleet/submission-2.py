class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Zip together position and speed
        zipped = list(zip(position, speed))
        zipped.sort(reverse = True)

        res = 0
        prev = 0

        for pos, s in zipped:
            time = (target - pos) / s
            if time > prev:
                res += 1
                prev = time
        
        return res



