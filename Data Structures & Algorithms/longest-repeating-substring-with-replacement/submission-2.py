class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n=len(s)
        ans=0
        
        for l in range(n):
            dic=defaultdict(int)
            max_freq=0
            for r in range(l,n):
                c=s[r]
                dic[c]+=1
                max_freq=max(max_freq,dic[c])
                cl=r-l+1
                changes=cl-max_freq
                if changes<=k:
                    ans=max(ans,cl)
                else:
                    break
        return ans



            



            

        