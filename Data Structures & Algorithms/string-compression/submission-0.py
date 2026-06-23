class Solution:
    def compress(self, chars: List[str]) -> int:
        
        n=len(chars)
        i=0
        s=""
        

        while i<n:
            s=s+chars[i]
            i=i+1
            l=1

            while i<n and chars[i]==chars[i-1]:
                l=l+1
                i=i+1
                
            if l>1:
                s=s+str(l)
        chars[:] = list(s)
        return len(chars)
            

        