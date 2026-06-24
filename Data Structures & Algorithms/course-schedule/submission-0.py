from collections import defaultdict
from pprint import pprint

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)

        for vertex, neigh in prerequisites:
            preMap[vertex].append(neigh)
        
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                # found cycle
                return False
            
            if preMap[crs] == []:
                return True
            
            visiting.add(crs)
            
            for neigh in preMap[crs]:
                if not dfs(neigh):
                    return False
            
            visiting.remove(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


