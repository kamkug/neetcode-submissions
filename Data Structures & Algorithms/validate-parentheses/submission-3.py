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
                stack_open_brace = stack.pop()
     
                if open_brace != stack_open_brace:
                    return False
            else:
                stack.append(c)
                

        
        return len(stack) == 0