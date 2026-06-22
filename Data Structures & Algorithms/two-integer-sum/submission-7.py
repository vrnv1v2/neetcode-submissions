class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic=defaultdict(int)
        for i in range(len(nums)):
            dic[nums[i]]=i
        for i in range(len(nums)):
            d=target-nums[i]
            if d in dic and dic[d]!=i:
                return [i,dic[d]]
    
             