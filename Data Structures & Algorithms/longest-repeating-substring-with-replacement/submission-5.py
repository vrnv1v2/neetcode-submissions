class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n=len(s)
        res=0
        dic=defaultdict(int)
        l=0
        maxf=0
        for r in range(n):
            dic[s[r]]+=1
            maxf=max(maxf,dic[s[r]])
            while (r-l+1)-maxf > k:
                dic[s[l]]-=1
                l=l+1
            res=max(res,r-l+1)
        return res
        

        
        



            



            

        