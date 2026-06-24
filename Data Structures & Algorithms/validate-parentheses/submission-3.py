class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        stack=[]
        key={")":"(","]":"[", "}":"{"}
        for i in s:
            if i in key:
                if stack and stack[-1]==key[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
                
            
        
        
        
        


        