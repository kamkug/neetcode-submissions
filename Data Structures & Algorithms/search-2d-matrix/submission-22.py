class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False

        top, bottom = 0, len(matrix)-1

        while top <= bottom:
            row = (top+bottom) // 2

            if target < matrix[row][0]:
                bottom = row-1
            elif target > matrix[row][-1]:
                top = row+1
            else:
                break

        row = (top+bottom) // 2
        left, right = 0, len(matrix[row])-1

        while left <= right:
            mid = (left+right) // 2

            if target < matrix[row][mid]:
                right = mid-1
            elif target > matrix[row][mid]:
                left = mid+1
            else:
                return True

        return False  