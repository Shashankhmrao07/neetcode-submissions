class MinStack:

    def __init__(self):
        self.stack = []
        self.min_Stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_Stack[-1] if self.min_Stack else val)
        self.min_Stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_Stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_Stack[-1]
        
