class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = set()

        for n in nums:
            if n in dups:
                return True
            dups.add(n)

        return False