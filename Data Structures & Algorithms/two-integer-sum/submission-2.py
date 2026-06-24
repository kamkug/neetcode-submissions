class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for i in range(len(nums)):
            # print(f"'nums[i]' is not in 'm' = {nums[i] not in m},  {target-nums[i]}, {m}", )
            if nums[i] not in m:
                m[target-nums[i]] = i
                continue

            return [m[nums[i]], i]

        return []