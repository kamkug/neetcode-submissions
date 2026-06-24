class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors_counts = [0, 0, 0]

        for n in nums:
            colors_counts[n] += 1
        
        i = 0
        for color in range(0, len(colors_counts)):
            for _ in range(colors_counts[color]):
                nums[i] = color
                i += 1
