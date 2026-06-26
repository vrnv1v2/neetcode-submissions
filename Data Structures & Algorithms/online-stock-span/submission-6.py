class StockSpanner:

    def __init__(self):
        self.stack=[]
        
        

    def next(self, price: int) -> int:
        span=1
        res=[]
        while self.stack and self.stack[-1][1]<=price:
            p,q=self.stack.pop()
            span=span+p
        self.stack.append([span,price])
        return span

       
    
        
            
                


            
           
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)