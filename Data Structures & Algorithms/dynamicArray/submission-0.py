class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.array = self.capacity * [0]

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()

        self.array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        self.length -= 1
        
        return self.array[self.length]

    def resize(self) -> None:
        self.capacity = self.capacity*2
        new_array = self.capacity * [0]
        
        for idx, element in enumerate(self.array):
            new_array[idx] = element
        
        self.array = new_array

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity