class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # space efficien due to O(1)
        i = 0  # read pointer
        write = 0  # write pointer

        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b),  # Truncate toward zero
        }

        for token in tokens:

            if token in ops:
                b = tokens[write-1]
                a = tokens[write-2]
                result = ops[token](a, b)

                # Overwrite last two numbers and operator with the result
                tokens[write-2] = int(result)
                write -= 1 # We've collapsed two numbers into one
            else:
                tokens[write] = int(token)
                write += 1
            
            
        return int(tokens[0])
