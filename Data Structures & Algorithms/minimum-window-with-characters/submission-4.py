from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        # 1. Initialize maps using defaultdict(int) to automatically handle missing keys
        countT = defaultdict(int)
        window = defaultdict(int)
        
        for c in t:
            countT[c] += 1

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        
        for r in range(len(s)):
            # 2. Add incoming character cleanly
            c = s[r]
            window[c] += 1

            # Check if this character fulfills our frequency requirement
            if c in countT and window[c] == countT[c]:
                have += 1

            # 3. Shrink phase: while the current window is fully valid
            while have == need:
                # Update our minimum window track (matches the Accumulator pattern!)
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # Cleanly kick out the character at the left edge
                window[s[l]] -= 1
                
                # If kicking it out drops us below what we need, we lose a matching character
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1
                
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""