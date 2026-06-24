from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = defaultdict(list)
        for c, pre in prerequisites:
            pre_map[c].append(pre)

        visited = set()

        def dfs(crs):
            if crs in visited:
                # Cycle found
                return False

            if pre_map[crs] == []:
                # We have already successfully explored this course
                return True
            
            visited.add(crs)

            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            
            visited.remove(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True