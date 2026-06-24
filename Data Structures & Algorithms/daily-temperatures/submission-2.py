class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        stack=[]
        
        
        for i,j in enumerate(temperatures):
            while stack and j>stack[-1][0]:
                p,q=stack.pop()
                ans[q]=i-q
            stack.append([j,i])
        return ans
            

            
            



        
                    

            



            
            



        