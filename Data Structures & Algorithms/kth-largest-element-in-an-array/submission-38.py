class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.helper(nums, k-1)
    
    def helper(self, nums, k):
        left, right = 0, len(nums)-1

        while True:
            if right <= left+1:
                if right == left+1 and nums[right] > nums[left]:
                    nums[right], nums[left] = nums[left], nums[right]
                return nums[k]
            
            j = self.partition(nums, left, right)

            if k <= j:
                right = j-1
            
            if k >= j:
                left = j+1
    
    def partition(self, nums, left, right):
        mid = (right+left) // 2
        nums[left+1], nums[mid] = nums[mid], nums[left+1]

        if nums[left] < nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        
        if nums[left+1] < nums[right]:
            nums[left+1], nums[right] = nums[right], nums[left+1]
        
        if nums[left] < nums[left+1]:
            nums[left], nums[left+1] = nums[left+1], nums[left]
        
        pivot = left+1
        i = left+1
        j = right

        while True:
            while True:
                i += 1
                if not nums[i] > nums[pivot]:
                    break
            
            while True:
                j -= 1
                if not nums[j] < nums[pivot]:
                    break
            
            if i > j:
                break
            
            nums[i], nums[j] = nums[j], nums[i]

        nums[pivot], nums[j] = nums[j], nums[pivot]
        return j
             
