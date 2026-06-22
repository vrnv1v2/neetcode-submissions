class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        l=0
        output=[]
        for i in range(n-k+1):
            mv=nums[i]
            for j in range(i,i+k):
                mv=max(mv,nums[j])
            output.append(mv)
        return output

        