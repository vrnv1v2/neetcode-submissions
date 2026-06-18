class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def counting_sort():
            c=defaultdict(int)
            minval,maxval=min(nums),max(nums)
            for i in range(len(nums)):
                c[nums[i]]+=1
            j=0
            for i in range(minval,maxval+1):
                while c[i]:
                    c[i]=c[i]-1
                    nums[j]=i
                    j=j+1
        counting_sort()
        return nums
        