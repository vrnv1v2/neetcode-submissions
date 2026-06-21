class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        l=0
        
        ans=0
        for r in range(1,n):
            p=0
            if prices[r]>prices[l]:
                p=p+prices[r]-prices[l]
                ans=max(ans,p)
            else:
                l=r
        return ans
                
            





        
        



        