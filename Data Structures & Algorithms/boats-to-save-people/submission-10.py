class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        minval=min(people)
        maxval=max(people)
        count=defaultdict(int)
        n=len(people)
        nums=[]
        for i in range(n):
            count[people[i]]+=1
        for i in range(minval,maxval+1):
            while count[i]>0:
                nums.append(i)
                count[i]-=1
        l=0
        r=n-1
        k=0
        while l<=r:
            
                sum=nums[l]+nums[r]
                if sum<=limit:
                    k+=1
                    l=l+1
                    r=r-1
                else:
                    r=r-1
                    k=k+1
                
                if l==r:
                    k=k+1
                    break
                
        
            

        return k
            


        