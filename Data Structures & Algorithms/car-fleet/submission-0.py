class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Zip together position and speed
        zipped = list(zip(position, speed))
        zipped.sort(reverse = True)

        arrivals = [(target - pos) / s for (pos, s) in zipped]
        
        res = len(arrivals)
        prev = -1
        print(arrivals)
        for i in range(len(arrivals)):
            if arrivals[i] <= prev:
                res -= 1
            prev = max(arrivals[i], prev)
        
        return res



