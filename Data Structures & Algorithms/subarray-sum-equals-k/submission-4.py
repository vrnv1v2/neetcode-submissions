class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic=defaultdict(int)
        dic[0]=1
        s1=0
        ans=0
        for i in nums:
            s1=s1+i
            d=s1-k
            ans=ans+dic[d]

            dic[s1]+=1
        return ans

        
        
        





        

            

        