class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        n=len(strs)
        s=strs[0]
        for i in range(1,len(strs)):
            j=0
            while j<min(len(s),len(strs[i])):
                if s[j]!=strs[i][j]:
                    break
                j=j+1
            s=s[:j]
        return s


        