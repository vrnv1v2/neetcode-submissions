class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        n=len(s)
        mv=0
        dic=defaultdict(int)
        for r in range(n):
            dic[s[r]]+=1
            while dic[s[r]]>1:
                dic[s[l]]-=1
                l=l+1
                if dic[s[l]]==0:
                    del dic[s[l]]
            
            mv=max(mv,r-l+1)
        return mv
        

            

        