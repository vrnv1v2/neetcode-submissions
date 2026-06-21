class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1)
        n2=len(s2)
        if n1>n2:
            return False
        base=defaultdict(int)
        for i in range(n1):
            base[s1[i]]+=1
        l=0
        dic=defaultdict(int)
        for r in range(n2):
            dic[s2[r]]+=1
            if r-l+1>n1:
                dic[s2[l]]-=1
                if dic[s2[l]]==0:
                    del dic[s2[l]]
                l=l+1
            if dic==base:
                return True
        
        return False


            





              


        




        