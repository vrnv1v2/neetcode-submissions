class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n=len(arr)
        l=0
        r=n-1
        while (r-l)>=k:
            if abs(x-arr[l])<= abs(x-arr[r]):
                r=r-1
            else:
                l=l+1
        return arr[l:r+1]

            


        


        