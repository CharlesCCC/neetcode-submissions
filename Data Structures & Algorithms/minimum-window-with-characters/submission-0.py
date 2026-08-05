class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #edge case
        if t == "" or len(s) < len(t):
            return ""
        
        #two pointers + dict/map 
        # two pointers/sliding window: 
        # right pointer keep moving, increase counter if seem one char until all included 
        # left pointer shrink (keep track of the minimum window)
        
        countT = defaultdict(int)
        for c in t:
            countT[c] += 1 
        
        window = defaultdict(int)
        have = 0
        need = len(countT)

        res = [-1,-1]
        resLen = float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] += 1
            if c in countT and window[c] == countT[c]:
                # valid within the window 
                have += 1 

            while have == need:
                # update the result for now 
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                # shrink the window 
                window[s[l]] -= 1  #decreae the count 
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1   #decrease have 
                l += 1

        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""


