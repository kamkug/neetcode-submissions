class LRUCache:

    def __init__(self, capacity: int):
        self.cache = []
        self.cap = capacity

    def get(self, key: int) -> int:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                self.cache.append(self.cache.pop(i))
                return self.cache[-1][1]
        
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                self.cache.pop(i)
                break
        
        if len(self.cache) == self.cap:
            self.cache.pop(0)
        
        self.cache.append((key, value))
            