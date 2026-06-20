class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=0
        
        
        n=len(nums)
        k=n-1
        res=[]
        nums.sort()
        while l<n:
            if l>0 and nums[l]==nums[l-1]:
                l=l+1
                continue

            r=l+1
            k=n-1
            while r<k:
                if nums[l]+nums[r]+nums[k]==0:
                    res.append([nums[l],nums[r],nums[k]])
                    r=r+1
                    k=k-1
                    while r < k and nums[r] == nums[r - 1]:
                        r = r + 1
                elif nums[l]+nums[r]+nums[k]>0:
                    k=k-1
                elif nums[l]+nums[r]+nums[k]<0:
                    r=r+1
            l=l+1
            
        return res


                    

       
                



        



        