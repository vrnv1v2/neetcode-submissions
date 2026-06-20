class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=0
        l2=0
        ans=""
        i=0
        while i < min(len(word1),len(word2)):
            ans=ans+word1[l1]
            ans=ans+word2[l2]
            l1+=1
            l2+=1
            i=i+1
        while l1<len(word1):
            ans=ans + word1[l1]
            l1+=1
        while(l2<len(word2)):
            ans=ans+word2[l2]
            l2+=1
        return ans

        