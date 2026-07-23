class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0] #initial str 
        for i in range(1, len(strs)):
            j = 0
            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]: #check char by char 
                    break
                j += 1
            prefix = prefix[:j]
        return prefix
