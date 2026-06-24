# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []

        for i in range(len(pairs)):
            j = i - 1

            while j >= 0 and pairs[j].key > pairs[j+1].key:
                pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
                j -= 1
            
            res.append(pairs[:])

        return res
    
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []

        def recursion(n):
            if n < 0:
                return

            recursion(n-1)

            last = pairs[n]
            j = n-1

            while j >= 0 and pairs[j].key > last.key:
                pairs[j+1] = pairs[j]
                j -= 1 
            
            pairs[j+1] = last

            res.append(pairs[:])
        
        recursion(len(pairs)-1)

        return res

            