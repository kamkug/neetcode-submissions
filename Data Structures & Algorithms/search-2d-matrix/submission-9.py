class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix)-1

        while L <= R:
            mid = (L+R) // 2

            if matrix[mid][-1] >= target:
                if target in {matrix[mid][0], matrix[mid][-1]}:
                    return True
                elif matrix[mid][0] < target:
                    return self.bin_search(matrix[mid], target)
                
                R = mid-1
            elif (mid+1) < len(matrix) and matrix[mid+1][0] <= target:
                if target in {matrix[mid+1][-1], matrix[mid+1][0]}:
                    return True
                elif matrix[mid+1][-1] > target:
                    return self.bin_search(matrix[mid+1], target)

                L = mid+1
            else:
                L = mid+1
        
        return False


    def bin_search(self, nums, target):
        L, R = 0, len(nums)

        while L <= R:
            mid = (L+R) // 2

            if nums[mid] < target:
                L = mid+1
            elif nums[mid] > target:
                R = mid-1
            elif nums[mid] == target:
                return True
        
        return False