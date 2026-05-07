class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crs_prereq = {i:[] for i in range(numCourses)}
        for crs, prereq in prerequisites:
            crs_prereq[crs].append(prereq)
        visiting = set()
        def dfs(crs):
            if crs in visiting:
                return False
            if crs_prereq[crs] == []:
                return True
            visiting.add(crs)
            for prereq in crs_prereq[crs]:
                if not dfs(prereq):
                    return False
            visiting.remove(crs)
            crs_prereq[crs] = []
            return True
        for crs in crs_prereq.keys():
            if not dfs(crs):
                return False
        return True