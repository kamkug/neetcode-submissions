class Solution:
        
    def partition(self, nums, left, right):
        mid = (right+left) >> 1
        nums[left+1], nums[mid] = nums[mid], nums[left+1]

        if nums[left] < nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        
        if nums[left+1] < nums[right]:
            nums[left+1], nums[right] = nums[right], nums[left+1]
        
        if nums[left] < nums[left+1]:
            nums[left], nums[left+1] = nums[left+1], nums[left]
        
        pivot = nums[left+1]
        i = left+1
        j = right

        while True:
            while True:
                i += 1
                if not nums[i] > pivot:
                    break
            
            while True:
                j -= 1
                if not nums[j] < pivot:
                    break
            
            if i > j:
                break
            
            nums[i], nums[j] = nums[j], nums[i]
        
        nums[left+1], nums[j] = nums[j], nums[left+1]

        return j
    
    def quick_select(self, nums, k):
        left = 0
        right = len(nums)-1

        while True:
            if right <= left+1:
                if right == left+1 and nums[right] > nums[left]:
                    nums[right], nums[left] = nums[left], nums[right]
                return nums[k]
            
            j = self.partition(nums, left, right)

            if j >= k:
                right = j-1
            
            if j <= k:
                left = j+1
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick_select(nums, k-1)