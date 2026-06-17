class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i,n in enumerate(nums):
            dic[n]=i
        for i,n in enumerate(nums):
            d=target-n
            if d in dic and dic[d]!=i:
                return [i,dic[d]]
        return []       