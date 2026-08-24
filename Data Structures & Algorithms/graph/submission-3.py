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
        visited.add(src)
        queue.append(src)

        while len(queue):
            for i in range(len(queue)):
                current = queue.popleft()
                if current == dst:
                    return True
                for conexion in self.graph[current]:
                    if conexion not in visited:
                        queue.append(conexion)
                        visited.add(conexion)

        return False
