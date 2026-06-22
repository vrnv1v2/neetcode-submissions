from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""

        
        dic=defaultdict(int)
        dic2=defaultdict(int)
        mv=float("inf")
        resa=[0]*2
        for i in range(len(t)):
            dic[t[i]]+=1
        n2=len(dic)
        n1=len(s)
        l=0
        c=0
        for r in range(n1):
            dic2[s[r]]+=1
            if s[r] in dic and dic2[s[r]]==dic[s[r]]:
                c=c+1
            while c==n2:
                if r-l+1<mv:
                    resa=[l,r]
                    mv=r-l+1
                dic2[s[l]]-=1
                
                
                if dic2[s[l]]==0:
                    del dic2[s[l]]
                if s[l] in dic and dic2[s[l]]<dic[s[l]]:
                    c=c-1
                l=l+1
        p,q=resa
        if mv == float("inf"):
            return ""
            
        else:
            return s[p:q+1]
            
                
                
                
