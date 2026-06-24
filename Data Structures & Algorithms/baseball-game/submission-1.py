class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores=[]
        s=0
        n=len(operations)
        for i in operations:
            if i=="+":
                scores.append(scores[-1]+scores[-2])
            elif i=="C":
                scores.pop()
            elif i=="D":
                scores.append(2*scores[-1])
            else:
                scores.append(int(i))
        return sum(scores)

        