class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        mp=0
        n=len(prices)
        for i in range(1,n):
            d=0
            d=prices[i]-prices[i-1]
            if d>0:
                p=p+d
            elif d==0:
                continue
            elif d<0:
                mp=mp+p
                p=0
        mp=mp+p
        
        return mp


        