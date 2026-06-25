class FreqStack:

    def __init__(self):
        self.stack=[]
        self.dic=defaultdict(int)#Counter
        self.group = defaultdict(list)## like Top K frequent idea
        self.mf=0
        

    def push(self, val: int) -> None:
        f=self.dic[val]+1
        self.dic[val]=f
        if f>self.mf:
            self.mf=f
        self.group[f].append(val)


        

    def pop(self) -> int:
        val = self.group[self.mf].pop()
        self.dic[val]-=1
        if not self.group[self.mf]:
            self.mf-= 1
        return val
        
                



        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
