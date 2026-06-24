from heapq import heapify, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapify(nums)

        res = 0
        for _ in range(k):
            res = heappop(nums)
        
        return -res