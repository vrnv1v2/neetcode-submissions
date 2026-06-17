from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        c2=defaultdict(list)        
        for i in range(len(strs)):
            c1=defaultdict(int)
            for j in range(len(strs[i])):
                c1[strs[i][j]]+=1
            c1_key = tuple(sorted(c1.items()))
            
            
            c2[c1_key].append(strs[i])
        return list(c2.values())




        