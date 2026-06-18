class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        r=len(matrix)
        c=len(matrix[0])
        self.smat=[[0]*(c+1) for i in range(r+1)]
        for i in range(r):
            p=0
            for j in range(c):
                p=p+matrix[i][j]
                a=self.smat[i][j+1]
                self.smat[i+1][j+1]=p+a
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,col1,row2,col2=row1+1,col1+1,row2+1,col2+1
        br=self.smat[row2][col2]
        a=self.smat[row2][col1-1]
        l=self.smat[row1-1][col2]
        tl=self.smat[row1-1][col1-1]
        return br-a-l+tl

        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)