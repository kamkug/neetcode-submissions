class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if 3 < len(tokens) < 1:
            return 0
 
        stack = []
        d = {
            '+': lambda a, b: a+b,
            '-': lambda a, b: a-b,
            '*': lambda a, b: a*b,
            '/': lambda a, b: int(a/b)
        }

        for token in tokens:
            if token in d:
                a, b = stack[-2:]
                stack = stack[:-2]
                stack.append(d[token](a, b))
            else:
                stack.append(int(token))
            print(stack)
        
        return stack[0]
