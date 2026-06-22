class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l=0
        n=len(s)
        dic=defaultdict(int)
        mv=0
        res=0
        for r in range(n):
            dic[s[r]]+=1
            mv=max(mv,dic[s[r]])
            while (r-l+1-mv)>k:
                dic[s[l]]-=1
                l=l+1
                if dic[s[l]]==0:
                    del dic[s[l]]
            res=max(res,r-l+1)
        return res
        
        

        

        
        



            



            

        