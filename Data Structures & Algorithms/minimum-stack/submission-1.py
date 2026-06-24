class MinStack:

    def __init__(self):
        self.stack=[]
        self.temp=[]
        
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val=min(val,self.temp[-1] if self.temp else val)
        self.temp.append(val)
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        self.temp.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        return self.temp[-1]
        

        
