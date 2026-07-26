class Solution:
    def isValid(self, s: str) -> bool:
        # two pointer or stack 
        stack = []
        closeToOpen = {")" : "(", "]": "[", "}" : "{"}

        for c in s: 
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop() # this is valid pair 
                else:
                    return False 
            else:
                stack.append(c)
        
        return True if not stack else False