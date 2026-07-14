class Solution:
    def findMin(self, nums: List[int]) -> int:
        left , right = 0 , len(nums)-1
        res = nums[0]
        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break

            mid = (left + right)//2
            # is the mid part of left sorted arr?
            # if yes then search in right part
            # as every element in left sorted arr > right sorted arr
            res = min(res, nums[mid])
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return res
            