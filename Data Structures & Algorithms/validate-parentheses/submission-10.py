class Solution:
    def isValid(self, s: str) -> bool:
        brackets_mapping = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        stack = []

        for char in s:
            if stack and char in brackets_mapping:
                if stack.pop() != brackets_mapping[char]:
                    return False
            else:
                stack.append(char)
        
        return not stack
            