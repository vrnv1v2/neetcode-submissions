class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic=defaultdict(int)
        dic2=defaultdict(int)
        n=len(nums)
        if not nums:
            return 0
        else:
            minv,maxv=min(nums),max(nums)
        res=[]
        j=0
        p=1
        max_streak=1
        for i in range(n):
            dic[nums[i]]+=1
        for i in range(minv,maxv+1):
            while dic[i]:
                dic[i]-=1
                nums[j]=i
                j=j+1
        for i in range(1,n):
            s=0
            s=nums[i]-nums[i-1]
            if s==1:
                p=p+1
            elif s==0:
                continue
            else:
                max_streak = max(max_streak, p)
                p = 1
        max_streak = max(max_streak, p)
        
        return max_streak

            



        