class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        s=0
        ans=0
        l=0
        r=n-1
        mod = 10**9 + 7
        while l<=r:
            s=nums[l]+nums[r]
            if s>target:
                r=r-1
            
            else:
                ans += (2 ** (r - l)) % mod
                l=l+1
                
               
        return ans%mod



        