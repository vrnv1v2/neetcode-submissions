class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        l=0
        
        
        n=len(nums)
        m=n-1
        res=[]
        while l<n:
            if l>0 and nums[l]==nums[l-1]:
                l=l+1
                continue
            r=l+1
            while r<n:
                if r>l+1 and nums[r]==nums[r-1]:
                    r=r+1
                    continue
                k=r+1
                m=n-1
                while k<m:
                    sum=nums[l]+nums[r]+nums[k]+nums[m]
                    if sum == target:
                         res.append([nums[l],nums[r],nums[k],nums[m]])
                         k=k+1
                         m=m-1
                         while k < m and nums[k] == nums[k - 1]:
                            k = k + 1
                    elif sum>target:
                        m=m-1
                    elif sum<target:
                        k=k+1
                r=r+1
            l=l+1
        return res


                


        
        