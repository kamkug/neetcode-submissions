class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        
        if len(tokens) < 3:
            return -1

        math_functions = {
            '+': lambda a, b: a+b,
            '-': lambda a, b: a-b,
            '*': lambda a, b: a*b,
            '/': lambda a, b: a // b if a >= 0 and b >= 0 else -(-a // b)
        }
        numbers = []

        for token in tokens:
            if token in math_functions:
                if len(numbers) < 2:
                    return False

                b = numbers.pop()
                a = numbers.pop()
                print(f'{a} {token} {b} = {math_functions[token](a, b)}')
                numbers.append(math_functions[token](a, b))
            else:
                numbers.append(int(token))
        
        return numbers[0]
