class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right):
            # Simple pivot selection - just use rightmost
            pivot = nums[right]
            i = left
            for j in range(left, right):
                if nums[j] >= pivot:  # >= for kth largest
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[right] = nums[right], nums[i]
            return i
        
        def quickselect(k):
            left, right = 0, len(nums) - 1
            
            while left < right:  # Simplified condition
                pivot_idx = partition(left, right)
                
                if pivot_idx == k:
                    return nums[k]
                elif pivot_idx > k:
                    right = pivot_idx - 1
                else:  # pivot_idx < k
                    left = pivot_idx + 1
            
            return nums[left]  # When left == right, we found it
        
        return quickselect(k - 1)