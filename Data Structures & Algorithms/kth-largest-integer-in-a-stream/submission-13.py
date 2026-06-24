class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        for num in nums:
            self.add(num)
        
        print(self.heap)

    def add(self, val: int) -> int:
        self.heap.append(val)
        i = len(self.heap)-1

        while i > 0 and self.heap[i] < self.heap[(i-1)//2]:
            tmp = self.heap[(i-1)//2]
            self.heap[(i-1)//2] = self.heap[i]
            self.heap[i] = tmp
            i = (i-1)//2
        
        if len(self.heap) > self.k:
            self.pop()
        
        return self.heap[0]
    
    def pop(self):
        i = 0
        self.heap[i] = self.heap.pop()

        while (i*2)+1 < len(self.heap):
            if ((i*2)+2 < len(self.heap) and
                self.heap[(i*2)+2] < self.heap[(i*2)+1] and
                self.heap[(i*2)+2] < self.heap[i]):

                tmp = self.heap[(i*2)+2]
                self.heap[(i*2)+2] = self.heap[i]
                self.heap[i] = tmp
                i = (i*2)+2
            elif self.heap[(i*2)+1] < self.heap[i]:
                tmp = self.heap[(i*2)+1]
                self.heap[(i*2)+1] = self.heap[i]
                self.heap[i] = tmp
                i = (i*2)+1
            else:
                break



        
