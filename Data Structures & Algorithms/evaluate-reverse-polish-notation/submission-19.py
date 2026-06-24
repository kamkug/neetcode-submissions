class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        math_functions = {
            '+': lambda a, b: a+b,
            '-': lambda a, b: a-b,
            '*': lambda a, b: a*b,
            '/': lambda a, b: int(a/b)
        }
        numbers = []

        for token in tokens:
            if token in math_functions:
                b = numbers.pop()
                a = numbers.pop()
                numbers.append(math_functions[token](a, b))
            else:
                numbers.append(int(token))
        
        return numbers[0]
