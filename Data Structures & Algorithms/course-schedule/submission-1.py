from collections import defaultdict
from pprint import pprint

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for v, p in prerequisites:
            preMap[v].append(p)
        
        visited = set()

        def dfs(crs):
            if crs in visited:
                # found cycle
                return False
            
            if preMap[crs] == []:
                return True
            
            visited.add(crs)

            for c in preMap[crs]:
                if not dfs(c):
                    return False
            visited.remove(crs)
            preMap[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True