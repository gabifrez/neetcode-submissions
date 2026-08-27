class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {}
        for i in range(n):
            graph[i] = set()
        for edge in edges:
            graph[edge[0]].add(edge[1])

        visited = set()
        path = set()
        result = []

        
        def dfs(node):
            if node in path:
                return False
            if node in visited:
                return True
            path.add(node)
            visited.add(node)

            for conexion in graph[node]:
                if not dfs(conexion):
                    return False
            path.remove(node)
            result.append(node)
            return True

        for i in range(n):
            if not dfs(i):
                return []
        result.reverse()
        return result
