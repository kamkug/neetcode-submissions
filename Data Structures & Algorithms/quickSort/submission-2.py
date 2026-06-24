# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quick_sort_helper(pairs, s, e)

        return pairs
    
    def quick_sort_helper(pairs, s, e):
        if s >= e:
            return
        
        pivot = pairs[e-1]
        left = s

        for k in range(s, e):
            if pairs[k].key < pivot.key:
                pairs[k], pairs[left] = pairs[k], pairs[left]
                left += 1
        

        pairs[e-1] = pairs[left]
        pairs[left] = pivot

        quick_sort_helper(pairs, s, left-1)
        quick_sort_helper(pairs, s, left+1)







































    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quick_sort(pairs, 0, len(pairs)-1)
        return pairs
    
    def quick_sort(self, arr: List[Pair], s: int, e: int) -> None:
        if e-s+1 <= 1:
            return arr
        
        pivot = arr[e]
        left = s

        for i in range(s, e):
            if arr[i].key < pivot.key:
                tmp = arr[left]
                arr[left] = arr[i]
                arr[i] = tmp
                left += 1

        arr[e] = arr[left]
        arr[left] = pivot

        # sort left side
        self.quick_sort(arr, s, left-1)
        # sort right side
        self.quick_sort(arr, left+1, e)

  
