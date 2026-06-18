class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=defaultdict(int)
        n=len(nums)
        f=[[]for i in range(n+1)]
        for i in range(n):
            c[nums[i]]+=1
        for i,j in c.items():
            f[j].append(i)
        r=[]
        for i in range(len(f)-1,0,-1):
            for j in f[i]:
                r.append(j)
                if len(r)==k:
                    return r

            


    

        