class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # faster approach
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

        
        # brute force - time limit exceeds
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False