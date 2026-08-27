class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i] = set()
        for (dst, src) in prerequisites:
            graph[src].add(dst)
        
        visited = set()
        path = set()

        def dfs(node):
            if node in path:
                return False
            if node in visited:
                return True
            visited.add(node)
            path.add(node)

            for conexion in graph[node]:
                if not dfs(conexion):
                    return False
            path.remove(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True