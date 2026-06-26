class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        res=r
        while l<=r:
            m=(l+r)//2
            cd=1
            cc=0
            for w in weights:
                if cc+w>m:
                    cd+=1
                    cc=0
                cc=cc+w
            if cd<=days:
                res=m
                r=m-1
            else:
                l=m+1
        return res




        