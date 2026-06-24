class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0

        for num in nums:
            tmp = two
            two = max(num+one, two)
            one = tmp
        
        return two