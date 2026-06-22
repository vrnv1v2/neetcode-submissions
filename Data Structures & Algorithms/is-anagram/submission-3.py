from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        n1=len(s)
        n2=len(t)
        d1=defaultdict(int)
        d2=defaultdict(int)
        for i in range(len(s)):
            d1[s[i]]+=1
            d2[t[i]]+=1
        if d1==d2:
            return True
        else:
            return False