class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        s=sum(piles)
        n=len(piles)
        ma=piles[n-1]
       
        l=1
        r=ma
        
        while l<=r:
            m=(l+r)//2
            su=0
            for p in piles:
                su=su+(p+m-1)//m
            if su>h:
                l=m+1
            else:
                res=m
                r=m-1
            


        return res 




        