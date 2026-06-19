class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        dicr=defaultdict(int)
        dicc=defaultdict(int)
        dicb=defaultdict(int)
        for i in range(9):
            for j in range(9):
                val=board[i][j]
                if val!=".":
                    dicr[(i,val)]+=1
                
                    dicc[(j,val)]+=1
                    box_row = i // 3
                    box_col = j // 3
                   
                    dicb[(box_row, box_col, val)] += 1
        for k, v in dicr.items():
            if v > 1:
                return False
                
        for k, v in dicc.items():
            if v > 1:
                return False
        for k,v in dicb.items():
            if v>1:
                return False
        return True
                


           
        
            



        