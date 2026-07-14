class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        
        for i in range(len(nums)):
            runningCount = 0
            for j in range(i, len(nums)):
                if nums[j] == 1:
                    runningCount+=1
                else:
                    break
            maxCount = max(maxCount, runningCount)
           
        return maxCount
