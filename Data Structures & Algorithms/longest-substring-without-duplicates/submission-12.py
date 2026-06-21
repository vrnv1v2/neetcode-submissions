class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        n=len(s)
        ans=0
        if not s:
            return 0

        m=set()
        for i in range(n):
            while s[i] in m:
                m.remove(s[l])
                l=l+1
            m.add(s[i])
            ans=max(ans,i-l+1)
        return ans

            

        