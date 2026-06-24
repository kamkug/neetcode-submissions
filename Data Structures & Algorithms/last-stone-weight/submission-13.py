class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_stone = max(stones)
        weights = [0] * (max_stone + 1)

        for s in stones:
            weights[s] += 1

        first = second = max_stone

        while first > 0:
            if weights[first] % 2 == 0:
                first -= 1
                continue
            
            j = min(first-1, second)

            while j > 0 and weights[j] == 0:
                j -= 1
            
            if j == 0:
                return first
            
            second = j
            weights[first] -= 1
            weights[second] -= 1
            weights[first-second] += 1
            first = max(first - second, second)
        
        return first