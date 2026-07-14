class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # linear O(n^2)
        res = cnt = 0
        for num in nums:
            if num == 0:
                res = max(res,cnt)
                cnt = 0
            else:
                cnt += 1
        return max(res, cnt)

        # brute force O(n^2)
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
