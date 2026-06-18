class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c=[0]*3
        for i in nums:
            c[i]=c[i]+1
        j=0
        for i in range(3):
            while c[i]:
                c[i]=c[i]-1
                nums[j]=i
                j=j+1
        
            
            

        
        