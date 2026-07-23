class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for s in details:
            age = int(s[11:13])
            if age > 60:
                res +=1
        return res