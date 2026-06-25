class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        
        for i in range(len(s)):
            if s[i]!="]":
                stack.append(s[i])
            else:
                k=""
                while stack[-1]!="[":
                    k=stack.pop()+k
                stack.pop()
                ans=""
                while stack and stack[-1].isdigit():
                    ans=stack.pop()+ans
                stack.append(int(ans)*k)
        return "".join(stack)
            




            

        