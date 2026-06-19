class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic=defaultdict(int)
        res=[]
        for i in range(len(nums)):
            dic[nums[i]]+=1
        for k,v in dic.items():
            if v > (len(nums))//3:
                res.append(k)
        return res

        

        