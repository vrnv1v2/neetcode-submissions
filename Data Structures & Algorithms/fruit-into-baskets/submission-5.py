class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        l=0
        mv=0
        s=0
        dic=defaultdict(int)
        for r in range(n):
            c=fruits[r]
            dic[c]+=1
            while len(dic) > 2:
                dic[fruits[l]]-=1
                if dic[fruits[l]]==0:
                    del dic[fruits[l]]
                l=l+1
            mv=max(mv,r-l+1)
            
        return mv

            

        
            


        