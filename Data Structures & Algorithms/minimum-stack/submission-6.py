class MinStack:

    def __init__(self):
        self.min_stack = []
        self.stack = []
        self.minim = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minim == None or self.minim > val:
            self.minim = val
        self.min_stack.append(self.minim)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        if self.min_stack:
            self.minim = self.min_stack[-1]
        else:
            self.minim = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minim
