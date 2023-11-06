class Solution(object):
    def maxSlidingWindow(self, nums, k):

        left = 0
        right = k

        Sums = []
        currentSum = 0

        while right <= len(nums):

            for i in range(k):
                currentSum += nums[i + left]

            Sums.append(currentSum)

            currentSum = 0

            left += 1
            right += 1

        return Sums





