class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l=0
        n=len(nums)
        r=n-1
        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                return True
            if nums[l]<nums[m]:
                if target>nums[m] or target<nums[l]:
                    l=m+1
                else:
                    r=m-1
            elif nums[l]>nums[m]:
                if target>nums[r] or target<nums[m]:
                    r=m-1
                else:
                    l=m+1
            else:
                l=l+1
        return False

        