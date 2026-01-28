class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        def helper(arr):
            #base case
            if len(arr)==len(nums):
                ans.append(arr[:])
                return
            else:
                for i in range(len(nums)): 
                    if nums[i] not in arr:
                        arr.append(nums[i])
                        helper(arr)
                        arr.pop()
        helper(subset)
        return ans