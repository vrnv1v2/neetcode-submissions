class Solution:
    def decodeString(self, s: str) -> str:
        stack1=[]
        stack2=[]
        c=""
        k=0
        for i in s:
            if i.isdigit():
                k=k*10 +int(i)
            elif i=="[":
                stack1.append(k)
                stack2.append(c)
                k=0
                c=""
            elif i=="]":
                temp=c
                c=stack2.pop()
                m=stack1.pop()
                c=c+temp*m
                

            
            else:
                c=c+i
        return c

        
        