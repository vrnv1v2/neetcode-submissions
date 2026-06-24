class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in asteroids:
            stack.append(i)
            while len(stack)>=2 and stack[-2]>0 and stack[-1]<0:
                if abs(stack[-2])==abs(stack[-1]):
                    stack.pop()
                    stack.pop()
                elif abs(stack[-2])>abs(stack[-1]):
                    stack.pop()
                elif abs(stack[-2])<abs(stack[-1]):
                    temp=stack.pop()
                    stack.pop()
                    stack.append(temp)
        return stack



        