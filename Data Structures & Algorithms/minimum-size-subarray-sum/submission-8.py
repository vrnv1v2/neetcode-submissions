class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        if not nums:
            return 0
        l=0
        s=0
        mv=float("inf")
        dic=defaultdict(int)
        for r in range(n):
            s=s+nums[r]
            while s>=target:
                mv=min(r-l+1,mv)
                s=s-nums[l]
                l=l+1
        if mv==float("inf"):
            return 0
        else: 
            return mv
            
        
            
        

            
            
            
            

        




        