from heapq import heappush, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = k-1
        
        def quick_select(l, r):

            pivot = nums[r]
            p = l

            for i in range(l, r):
                if nums[i] >= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
                
            nums[r], nums[p] = nums[p], nums[r]

            if p > k:
                return quick_select(l, p-1)
            elif p < k:
                return quick_select(p+1, r)
            else:
                return nums[p]
        
        return quick_select(0, len(nums)-1)




        
        