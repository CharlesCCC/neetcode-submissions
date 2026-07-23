class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #split to words 
        ws = s.split()

        return len(ws[-1])