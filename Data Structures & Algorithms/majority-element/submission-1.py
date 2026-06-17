from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        c=defaultdict(int)
        for i in range(n):
            c[nums[i]]+=1
        for k,v in  c.items():
            if v > n/2:
                return k
        return
            
        