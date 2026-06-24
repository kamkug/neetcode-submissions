class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        stack = []

        for cp in s:
            if cp in d and stack and d[cp] == stack[-1]:
                stack.pop()
            else:
                stack.append(cp)

        return len(stack) == 0