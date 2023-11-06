class Solution:
    def productExceptSelf(self, nums):
        Results = []

        acc = 1
        for n in nums:
            Results.append(acc)
            acc *= n

        acc = 1
        for i in reversed(range(len(nums))):
            Results[i] *= acc
            acc *= nums[i]

        return Results