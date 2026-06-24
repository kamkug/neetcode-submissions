class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = []

    def get(self, key: int) -> int:
        for idx in range(len(self.cache)):
            if self.cache[idx][0] == key:
                tmp = self.cache.pop(idx)
                self.cache.append(tmp)
                return tmp[1]
        
        return -1

    def put(self, key: int, value: int) -> None:
        for idx in range(len(self.cache)):
            if self.cache[idx][0] == key:
                tmp = self.cache.pop(idx)
                self.cache.append(tmp)
                tmp[1] = value
                return

        if len(self.cache) == self.capacity:
            self.cache.pop(0)

        self.cache.append([key, value])
