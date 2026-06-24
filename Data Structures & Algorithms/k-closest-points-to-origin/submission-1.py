import math

from heapq import heappop


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_min_heap = []
        result = []

        for point in points:
            self.heappush(points_min_heap, point)
        
        for _ in range(k):
            result.append(self.heappop(points_min_heap))
        
        return result
    

    def heappush(self, heap: List[[List[int]]], point: List[List[int]]):
        if not heap:
            heap.append(point)
            return

        origin = [0, 0]
        heap.append(point)
        idx = len(heap)-1

        while idx > 0 and math.dist(origin, heap[idx]) < math.dist(origin, heap[(idx-1)//2]):
            heap[idx], heap[(idx-1) // 2] = heap[(idx-1) // 2], heap[idx]
            idx = (idx-1) // 2
    
    def heappop(self, heap: List[List[int]]) -> int:
        if not heap:
            return -1
        
        if len(heap) == 1:
            return heap.pop()

        origin = [0, 0]
        idx = 0
        result = heap[idx]
        heap[idx] = heap.pop()

        while idx*2 + 1 < len(heap):
            left = idx*2 + 1
            right = idx*2 + 2

            if (right < len(heap) and 
                math.dist(origin, heap[right]) < math.dist(origin, heap[left]) and 
                math.dist(origin, heap[right]) < math.dist(origin, heap[idx])):

                heap[idx], heap[right] = heap[right], heap[idx]
                idx = right
            elif math.dist(origin, heap[left]) < math.dist(origin, heap[idx]):
                heap[idx], heap[left] = heap[left], heap[idx]
                idx = left
            else:
                break
        
        return result
        

