class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        visited = set()
        adjList = {k :[] for k in range(n)}
        for n1,n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)   
            for child in adjList[node]:
                if child == prev:
                    continue
                if not dfs(child, node):
                    return False
            return True
    
        return dfs(0, -1) and len(visited) == n
