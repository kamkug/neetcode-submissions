class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        self.heappush(val)

        if len(self.heap) > self.k:
            self.heappop()
        
        return self.heap[0]
    
    def heappush(self, val: int) -> None:
        self.heap.append(val)
        i = len(self.heap) - 1

        while i > 0 and self.heap[i] < self.heap[(i-1) // 2]:
            self.heap[i], self.heap[(i-1) // 2] = self.heap[(i-1) // 2], self.heap[i]
            i = (i-1) // 2
    
    def heappop(self) -> None:
        i = 0
        self.heap[i] = self.heap.pop()

        while i*2 + 1 < len(self.heap):
            if (i*2 + 2 < len(self.heap) and 
                self.heap[i*2 + 2] < self.heap[i*2 + 1] and 
                self.heap[i*2 + 2] < self.heap[i]):

                self.heap[i*2 + 2], self.heap[i] = self.heap[i], self.heap[i*2 + 2]
                i = i*2 + 2
            elif self.heap[i*2 + 1] < self.heap[i]:
                self.heap[i*2 + 1], self.heap[i] = self.heap[i], self.heap[i*2 + 1]
                i = i*2 + 1
            else:
                break

