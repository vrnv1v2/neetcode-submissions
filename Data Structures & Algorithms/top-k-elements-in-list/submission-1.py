class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=defaultdict(int)
        n=len(nums)
        for i in range(n):
            c[nums[i]]+=1
        pairs=list(c.items())
        pairs.sort(key=lambda x:x[1],reverse=True)
        return [pairs[i][0] for i in range(k)]
        
            


    

        