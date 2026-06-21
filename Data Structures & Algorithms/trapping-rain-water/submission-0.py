class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l=0
        r=len(height)-1
        lm=height[l]
        rm=height[r]
        ans=0
        while l<r:
            if lm<rm:
                l=l+1
                lm=max(lm, height[l])
                ans=ans+lm-height[l]
            else:
                r=r-1
                rm=max(rm,height[r])
                ans=ans+rm-height[r]
        return ans
               
            
                  
            

            
            
        