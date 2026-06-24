class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        
        for c in s:
            if c in d:  # It's a closing bracket
                if not stack or stack.pop() != d[c]:
                    return False
            else:  # It's an opening bracket
                stack.append(c)
                
        return len(stack) == 0
