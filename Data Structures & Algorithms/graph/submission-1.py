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
        visited = set()

        def dfs(src, dst):
            visited.add(src)
            
            if src == dst:
                return True
            
            for neigh in self.adj_list[src]:
                if neigh not in visited:
                    if dfs(neigh, dst):
                        return True
            
            return False
        
        return dfs(src, dst)

