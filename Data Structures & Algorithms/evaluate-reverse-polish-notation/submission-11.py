def ceil(a, b):
    return -(a // b) 


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1 :
            return int(tokens[-1])
        if len(tokens) < 3:
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
                # a, b = stack[-2:]
                # stack = stack[:-2]
                b, a = stack.pop(), stack.pop()
                stack.append(d[token](a, b))
            else:
                stack.append(int(token))
        
        return stack[0]
