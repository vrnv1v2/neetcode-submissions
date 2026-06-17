from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Initialize both as defaultdicts
        countS, countT = defaultdict(int), defaultdict(int)

        # Look how clean this loop becomes:
        for i in range(len(s)):
            countS[s[i]] += 1
            countT[t[i]] += 1
            
        return countS == countT