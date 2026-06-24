class Solution:

    def partition(self, nums, left, right):                       # [5,6,4,2,3]
        mid = (left+right) // 2                                   # 2
        nums[left+1], nums[mid] = nums[mid], nums[left+1]         # [5,4,6,2,3]
        
        if nums[left] < nums[right]:
            nums[left], nums[right] = nums[right], nums[left]     # skip
        
        if nums[left+1] < nums[right]:
            nums[left+1], nums[right] = nums[right], nums[left+1] # skip
        
        if nums[left] < nums[left+1]:
            nums[left], nums[left+1] = nums[left+1], nums[left]   # skip

        pivot = nums[left+1]                                      # pivot = 4
        i = left+1                                                # i = 1
        j = right                                                 # j = 4

        while True:
            while True:
                i += 1                                            # i = 3
                if not nums[i] > pivot:
                    break
            
            while True:
                j -= 1                                            # j = 2
                if not nums[j] < pivot:
                    break
            
            if j < i:
                break
            
            nums[i], nums[j] = nums[j], nums[i]              
        
        nums[left+1], nums[j] = nums[j], nums[left+1]             # [5,6,4,2,3] 
        return j                                                  # 2

    def quick_select(self, nums, k):
        left, right = 0, len(nums)-1

        while True:
            if right <= left+1:
                if right == left+1 and nums[right] > nums[left]:
                    nums[right], nums[left] = nums[left], nums[right]
                
                return nums[k]

            j = self.partition(nums, left, right) # j = 5

            if j <= k:
                left = j+1   # left = 0
            
            if j >= k:
                right = j-1  # right = 1



    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick_select(nums, k-1)

