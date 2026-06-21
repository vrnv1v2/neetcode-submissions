class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        count=defaultdict(int)
        for i in range(n):
            if nums[i] in count and abs(i-count[nums[i]])<=k:
                return True
            count[nums[i]]=i
        return False
            


        