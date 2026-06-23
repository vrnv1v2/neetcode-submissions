class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=0
        n=len(nums)
        res=[]
        nums.sort()
        while l<n:
            
            if l>0 and nums[l]==nums[l-1]:
                l=l+1
                continue
            r=l+1
            k=n-1
            while r<k:
                s=nums[l]+nums[r]+nums[k]
                if s==0:
                    res.append([nums[l],nums[r],nums[k]])
                    r=r+1
                    k=k-1
                    while r < k and nums[r] == nums[r - 1]:
                        r = r + 1
                elif s<0:
                    r=r+1
                elif s>0:
                    k=k-1
            l=l+1
        return res


                    

       
                



        



        