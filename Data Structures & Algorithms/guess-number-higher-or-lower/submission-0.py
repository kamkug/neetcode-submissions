# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            curr = (l+r) // 2

            match guess(curr):
                case -1: r = curr-1
                case 1: l = curr+1
                case _: return curr
        
        return -1