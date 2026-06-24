class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        
        for c in s:
            if stack and (open_brace := d.get(c)):
                if open_brace != stack.pop():
                    return False
            else:
                stack.append(c)
                

        
        return len(stack) == 0
