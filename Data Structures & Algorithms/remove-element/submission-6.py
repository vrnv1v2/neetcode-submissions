class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        m=[]
        k=0
        for i in range(n):
            l=0
            if nums[i]==val:
                k=k+1
                l=l+1
            if l==0:
                m.append(nums[i])
        nums[:]=m
        return n-k


        

        
        