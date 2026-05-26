class MinStack:

    # def __init__(self):
    #     self.stack = []
    #     self.min_Stack = []
        

    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    #     if not self.min_Stack:
    #         self.min_Stack.append(val)
    #     else:
    #         self.min_Stack.append(min(self.min_Stack[-1], val))
        

    # def pop(self) -> None:
    #     self.stack.pop()
    #     self.min_Stack.pop()
        

    # def top(self) -> int:
    #     return self.stack[-1]
        

    # def getMin(self) -> int:
    #     return self.min_Stack[-1]
        
    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min = val
        else:
            if val > self.min:
                self.stack.append(val)
            else:
                self.stack.append(2 * val - self.min)
                self.min = val

    def pop(self) -> None:
        val = self.stack.pop()
        if val > self.min:
            return val
        else:
            self.min = 2 * self.min - val
            return self.min

    def top(self) -> int:
        val = self.stack[-1]
        if val > self.min:
            return val
        return self.min

    def getMin(self) -> int:
        return self.min
