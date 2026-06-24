# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []

        def recursion(n: int):
            if n == 0:
                return
            
            recursion(n-1)

            last = pairs[n-1]
            j = n-2

            while j >= 0 and pairs[j].key > last.key:
                pairs[j+1] = pairs[j]
                j -= 1
            
            pairs[j+1] = last
            res.append(pairs.copy())

        recursion(len(pairs))

        return res