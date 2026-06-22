class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=defaultdict(int)
        n=len(nums)
        res=[]
        f=[[] for i in range(n+1)]
        for i in range(n):
            dic[nums[i]]+=1
        for i,j in dic.items():
            f[j].append(i)
        for i in range(n,0,-1):
            for j in f[i]:
                res.append(j)
            if len(res)==k:
                return res
        return



            


    

        