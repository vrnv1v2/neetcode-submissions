class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic=defaultdict(int)
        for i in range(len(nums)):
            dic[nums[i]]+=1
        for i,j in dic.items():
            if dic[i]>1:
                return True
        return False

        