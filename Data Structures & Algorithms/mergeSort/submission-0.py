# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.merge_sort_helper(pairs, 0, len(pairs)-1)

        return pairs
    
    def merge_sort_helper(self, pairs: List[Pair], s: int, e: int):
        if s >= e:
            return
        
        m = (s + e) // 2

        self.merge_sort_helper(pairs, s, m)   # sort the left half
        self.merge_sort_helper(pairs, m+1, e) # sort the right half

        self.merge_lists(pairs, s, m, e)

    def merge_lists(self, pairs, s, m, e):
        left = pairs[s:m+1]
        right = pairs[m+1:e+1]
        l, r = 0, 0
        k = s

        while l < len(left) and r < len(right):
            if left[l].key <= right[r].key:
                pairs[k] = left[l]
                l += 1
            else:
                pairs[k] = right[r]
                r += 1
            k += 1
        
        while l < len(left):
            pairs[k] = left[l]
            l += 1
            k += 1

        while r < len(right):
            pairs[k] = right[r]
            r += 1
            k += 1
        



