class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        s=sum(piles)
        n=len(piles)
        ma=piles[n-1]
       
        l=1
        r=ma
        res=r
        
        while l<=r:
            m=(l+r)//2
            su=0
            for p in piles:
                su=su+math.ceil(float(p)/m)
            if su<=h:
                res=m
                r=m-1
            else:
                l=m+1
            

        return res 




        