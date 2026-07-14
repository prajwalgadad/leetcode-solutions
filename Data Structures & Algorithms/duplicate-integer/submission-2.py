class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # linar approach - O(n)
        hashMap = {}
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        
        for ele in hashMap.keys():
            if hashMap[ele] > 1:
                return True
        return False


        # faster approach - O(nlog(n))
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