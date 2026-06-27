class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            sa=1
            cs=0
            for i in nums:
                cs=cs+i
                if cs>largest:
                    sa=sa+1
                    if sa>k:
                        return False
                    cs=i
            return True



        l=max(nums)
        r=sum(nums)
        res=r
        mv=0
        while l<=r:
            m=(l+r)//2
            if canSplit(m):
                res=m
                r=m-1
            else:
                l=m+1
        return res





        