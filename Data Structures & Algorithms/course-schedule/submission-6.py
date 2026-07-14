class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for course in range(numCourses):
            graph[course] = []
        
        for c1, c2 in prerequisites:
            graph[c1].append(c2)

        visited = set() 
        def dfs(node):
            if graph[node] == []:
                return True
            if node in visited:
                return False
            visited.add(node)
            
            for course in graph[node]:
                if not dfs(course):
                    return False
            graph[course] = []
            visited.remove(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True




