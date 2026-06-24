# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def sort(arr, s, e):
            if e-s+1 <= 1:
                return
            
            m = (s+e) // 2

            sort(pairs, s, m)
            sort(pairs, m+1, e)

            self.merge_sides(arr, s, m, e)
        
        sort(pairs, 0, len(pairs)-1)
        return pairs
    
    def merge_sides(self, arr, s, m, e):
        left = arr[s:m+1]
        right = arr[m+1:e+1]

        l = r = 0
        k = s

        while l < len(left) and r < len(right):
            if left[l].key <= right[r].key:
                arr[k] = left[l]
                l += 1
            else:
                arr[k] = right[r]
                r += 1
            k += 1
        
        while l < len(left):
            arr[k] = left[l]
            l += 1
            k += 1
        
        while r < len(right):
            arr[k] = right[r]
            r += 1
            # k += 1