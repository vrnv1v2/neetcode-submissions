class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        l=0
        r=m-1
        while l<=r:
            s=(l+r)//2
            if matrix[s][-1]<target:
                l=s+1
            elif matrix[s][0]>target:
                r=s-1
            else:
                break
        if not(l<=r):
            return False
        s=(l+r)//2
        l=0
        r=n-1
        while l<=r:
            ss=(l+r)//2
            if target>matrix[s][ss]:
                l=ss+1
            elif target<matrix[s][ss]:
                r=ss-1
            else:
                return True
        return False
        

            
        