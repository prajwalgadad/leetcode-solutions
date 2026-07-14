class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, sum, comb):
            if sum == target and comb:
                res.append(comb[:])
                return
            if i>=len(nums) or sum > target:
                return

            comb.append(nums[i])
            dfs(i , sum + nums[i], comb)
            comb.pop()
            dfs(i+1 , sum, comb)
        
        dfs(0,0,[])
        return res