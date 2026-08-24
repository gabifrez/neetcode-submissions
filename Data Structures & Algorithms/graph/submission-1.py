
class Graph:
    
    def __init__(self):
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = set()
        if dst not in self.graph:
            self.graph[dst] = set()
        self.graph[src].add(dst)
    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph or dst not in self.graph[src]:
            return False
        self.graph[src].remove(dst)
        return True
    def hasPath(self, src: int, dst: int) -> bool:
        queue = deque()
        visited = set()
        queue.append(src)
        visited.add(src)
        while len(queue):
            for i in range(len(queue)):
                node = queue.popleft()
                if node == dst:
                    return True
                for conexion in self.graph[node]:
                    if conexion not in visited:
                        visited.add(conexion)
                        queue.append(conexion)
        return False

