class MinStack:

    def __init__(self):
           self.stack = [] 
           self.min_value = float('inf')    

    def push(self, val: int) -> None:
        if not self.stack:
            self.min_value = val
            self.stack.append(val)
            return
        
        if val < self.min_value:
            self.stack.append(2 * val - self.min_value)
            self.min_value = val
        else:
            self.stack.append(val)

        

    def pop(self) -> None:
        if not self.stack:
            return
        top = self.stack.pop()
        if top < self.min_value:
            self.min_value = 2 * self.min_value - top

        

    def top(self) -> int:
        if not self.stack:
            return None
        top = self.stack[-1]
        return self.min_value if top < self.min_value else top
        

    def getMin(self) -> int:
        return self.min_value if self.stack else None