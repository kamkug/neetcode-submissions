class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        stack = []

        for cp in s:
            if cp in d and stack:
                if d[cp] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(cp)

        return len(stack) == 0