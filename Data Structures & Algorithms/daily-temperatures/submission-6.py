class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)
        for i,j in  enumerate(temperatures):
            while stack and j>stack[-1][0]:
                p,q=stack.pop()
                res[q]=i-q
            stack.append([j,i])
        return res
        
        
            

            
            



        
                    

            



            
            



        