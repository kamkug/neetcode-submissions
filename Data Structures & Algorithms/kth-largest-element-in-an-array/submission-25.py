from heapq import heappush, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        heap = []

        for n in nums:
            heappush(heap, n)

            if len(heap) > k:
                heappop(heap)
        
        return heap[0]




        
        