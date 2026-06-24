from collections import defaultdict

class Graph:
    
    def __init__(self):
        self.adj_list = defaultdict(list)

    def addEdge(self, src: int, dst: int) -> None:
        self.adj_list[src].append(dst)
        print(self.adj_list)

    def removeEdge(self, src: int, dst: int) -> bool:
        for idx in range(len(self.adj_list[src])):
            if self.adj_list[src][idx] == dst:
                break
        else:
            return False
        
        self.adj_list[src].pop(idx)
        return True


    def hasPath(self, src: int, dst: int) -> bool:
        if src == dst:
            return True

        visited = set()
        q = deque()
        q.append(src)
        visited.add(src)

        while q:
            curr = q.popleft()

            for neigh in self.adj_list[curr]:
                if neigh == dst:
                    return True

                if neigh not in visited:
                    visited.add(neigh)
                    q.append(neigh)
        
        return False

