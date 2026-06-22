class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        l=0
        res=[]
        out=[]
        for r in range(n):
            res.append(nums[r])
            if (r-l+1)==k:
                out.append(max(res))
                res.pop(0)
                l=l+1
        return out
            


        