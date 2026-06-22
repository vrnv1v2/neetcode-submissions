class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1)
        n2=len(s2)
        if n1>n2:
            return False
        l=0
        dic=defaultdict(int)
        dic2=defaultdict(int)
        for i in range(n1):
            dic2[s1[i]]+=1
        for r in range(n2):
            dic[s2[r]]+=1
            while (r-l+1)>n1:
                dic[s2[l]]-=1
                
                if dic[s2[l]]==0:
                    del dic[s2[l]]
                l=l+1
                
            if dic==dic2:
                    return True
        return False

        
            
        


            





              


        




        