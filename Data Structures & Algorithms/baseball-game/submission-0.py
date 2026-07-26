class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for s in operations:
            if s == '+':
                stack.append(stack[-2] + stack[-1])
            elif s == 'D':
                stack.append(stack[-1] * 2)
            elif s == 'C':
                stack.pop()
            else:
                stack.append(int(s))
        
        res = 0
        while stack:
            res += stack.pop()
        
        return res