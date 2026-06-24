class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return

        res = self.stack.pop()

        if res == self.min_stack[-1]:
            self.min_stack.pop()
        
        return res

    def top(self) -> int:
        if not self.stack:
            return
        
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack:
            return    

        return self.min_stack[-1]    
