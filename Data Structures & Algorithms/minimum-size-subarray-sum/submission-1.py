class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        n=len(nums)
        res=float("inf")
        s=0
        for r in range(n):
            s=s+nums[r]
            while s>=target:
                res=min(r-l+1,res)
                s=s-nums[l]
                l+=1
        return 0 if res==float("inf") else res
            
            
        

            
            
            
            

        




        