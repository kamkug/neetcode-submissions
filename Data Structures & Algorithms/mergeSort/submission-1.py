# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def sort(start, end):
            if end-start + 1 <= 1:
                return
            
            mid = (start+end) // 2
            sort(start, mid)
            sort(mid+1, end)

            self.merge_sides(start, mid, end)

        sort(0, len(pairs)-1)
        return pairs
    
    def merge_sides(self, start, mid, end):
        left = pairs[start:mid+1]
        right = pairs[mid+1:end+1]

        l, r = 0, 0
        k = start

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


