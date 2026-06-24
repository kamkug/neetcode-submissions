# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def helper(pairs: List[Pair], s: int, e: int):
            if e-s+1 <= 1:
                return None
            
            pivot = pairs[e-1]
            left = s

            for i in range(s, e):
                if pairs[i].key < pivot.key:
                    pairs[left], pairs[i] = pairs[i], pairs[left]
                    left += 1
            
            pairs[e-1] = pairs[left]
            pairs[left] = pivot

            helper(pairs, s, left)
            helper(pairs, left+1, e)
            
        
        helper(pairs, 0, len(pairs))

        return pairs