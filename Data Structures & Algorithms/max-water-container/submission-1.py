class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans=0
        l=0
        n=len(heights)
        r=n-1
        while l<r:
            w=r-l
            h=min(heights[l],heights[r])
            ar=w*h
            ans=max(ar,ans)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return ans

            
        

        