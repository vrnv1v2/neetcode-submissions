class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1=0
        c2=0
        cand1, cand2 = None, None
        if not nums:
            return []
        res=[]
        for i in range(len(nums)):
            if nums[i]==cand1:
                c1+=1
            elif nums[i]==cand2:
                c2+=1
            elif c1==0:
                cand1=nums[i]
                c1=1
            elif c2==0:
                cand2=nums[i]
                c2=1
            else:
                c1-=1
                c2-=1
        threshold = len(nums) // 3
        
        for cand in [cand1, cand2]:
            if cand is not None and nums.count(cand) > threshold:
                res.append(cand)
                
        return res


        
        

        