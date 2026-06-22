from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        c=[0]*26
        d2=defaultdict(list)
        n=len(strs)
        for i in range(n):
            d1=defaultdict(int)

            for j in range(len(strs[i])): 
                c=strs[i][j]
                d1[ord(c)-ord("a")]+=1
            c2=tuple(sorted(d1.items()))
            d2[c2].append(strs[i])
        return list(d2.values())






        