class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bottom, top = 0, len(matrix)-1

        while bottom <= top:
            row = (bottom+top) // 2

            if target < matrix[row][0]:
                top = row-1
            elif target > matrix[row][-1]:
                bottom = row+1
            else:
                break
        else:
            return False
        
        
        left, right = 0, len(matrix[0])
        row = (bottom+top) // 2

        while left <= right:
            mid = (left+right) // 2

            if target < matrix[row][mid]:
                right = mid-1
            elif target > matrix[row][mid]:
                left = mid+1
            else:
                return True
        
        return False
            