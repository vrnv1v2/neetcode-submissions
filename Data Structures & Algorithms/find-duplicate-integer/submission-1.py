class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        l=1
        r=n
        ans=r
        def dup(d):
            s=0
            for i in nums:
                if i<=d:
                    s=s+1
            if s<=d:
                return True
            else:
                return False
        while l<=r:
            m=(l+r)//2
            if dup(m):
                l=m+1
            else:
                ans=m
                r=m-1
        return ans





        