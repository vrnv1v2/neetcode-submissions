class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp,rp=0,len(s)-1
        s=s.lower()
        while lp<rp:
            while lp<rp and not s[lp].isalnum():
                lp=lp+1
            while lp<rp and not s[rp].isalnum():
                rp=rp-1
            if s[lp]!=s[rp]:
                return False
            lp+=1
            rp-=1
        return True


        
            

        