# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quick_sort(pairs, 0, len(pairs)-1)
        return pairs

    def quick_sort(self, pairs, s, e):
        if e-s+1 <= 1:
            return pairs
        
        pivot = pairs[e]
        cursor = s
        
        for i in range(s, e):
            if pairs[i].key < pivot.key:
                tmp = pairs[cursor]
                pairs[cursor] = pairs[i]
                pairs[i] = tmp
                cursor += 1
        
        pairs[e], pairs[cursor] = pairs[cursor], pivot

        self.quick_sort(pairs, s, cursor-1)
        self.quick_sort(pairs, cursor+1, e)

