class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(position)
        res=[]
        for i in range(n):
            res.append([position[i],(target-position[i])/(speed[i])])
        res.sort(key=lambda x: x[0], reverse=True)
        stack=[]
        for i,j in res:
            stack.append(j)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)

            





        