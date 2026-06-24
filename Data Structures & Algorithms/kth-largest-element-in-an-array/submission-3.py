from heapq import heapify, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        heap = []
        for n in nums:
            self.heappush(heap, n)
            if len(heap) == k+1:
                self.heappop(heap)
        
        return heap[0]
    
    def heappush(self, heap, val):
        if not heap:
            heap.append(val)
            return

        heap.append(val)
        idx = len(heap)-1

        while idx > 0 and heap[idx] < heap[(idx-1) // 2]:
            heap[idx], heap[(idx-1) // 2] = heap[(idx-1) // 2], heap[idx]
            idx = (idx-1) // 2
    
    def heappop(self, heap):
        idx = 0
        heap[idx] = heap.pop()

        while idx*2+1 < len(heap):
            left = idx*2+1
            right = left+1

            if right < len(heap) and heap[right] < heap[left] and heap[right] < heap[idx]:
                heap[idx], heap[right] = heap[right], heap[idx]
                idx = right
            elif heap[left] < heap[idx]:
                heap[idx], heap[left] = heap[left], heap[idx]
                idx = left
            else:
                break



        
        