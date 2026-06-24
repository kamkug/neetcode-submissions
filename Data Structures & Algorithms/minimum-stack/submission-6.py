class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
            return

        for idx in range(len(self.min_stack)):
            if val <= self.min_stack[idx]:
                self.min_stack = self.min_stack[:idx+1] + [val] + self.min_stack[idx+1:]
                break

    def pop(self) -> None:
        v = self.stack.pop()

        for idx in range(len(self.min_stack)):
            if self.min_stack[idx] == v:
                self.min_stack = self.min_stack[:idx] + self.min_stack[idx+1:]
                break

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
        
