class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0

        new_array = [0] * (max(stones)+1)
        for s in stones:
            new_array[s] += 1
        
        first = second = max(stones)

        while first > 0:
            if new_array[first] % 2 == 0:
                first -= 1
                continue
            
            j = min(first-1, second)
            while j > 0 and new_array[j] == 0:
                j -= 1

            if j == 0:
                return first
            
            second = j
            new_array[first] -= 1
            new_array[second] -= 1
            new_array[first-second] += 1

            first = max(first-second, second)
        
        return first