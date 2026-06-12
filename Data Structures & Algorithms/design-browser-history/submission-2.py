class Node:
    def __init__(self, prev = None, val = None, next = None):
        self.prev = prev
        self.val = val
        self.next = next
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = Node(prev = Node(), val = homepage, next = Node())
        self.step_back = self.step_forward = 0

    def visit(self, url: str) -> None:
        self.history.next = Node(prev = self.history, val = url, next = Node())
        self.history = self.history.next
        self.step_forward = 0
        self.step_back += 1

    def back(self, steps: int) -> str:
        if steps > self.step_back:
            steps = self.step_back
        for i in range(steps):
            self.history = self.history.prev

        self.step_back -= steps
        self.step_forward += steps

        return self.history.val

    def forward(self, steps: int) -> str:
        if steps > self.step_forward:
            steps = self.step_forward
        for i in range(steps):
            self.history = self.history.next

        self.step_forward -= steps
        self.step_back += steps
        return self.history.val    


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)