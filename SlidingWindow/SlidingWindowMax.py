class Solution(object):
    def maxSlidingWindow(self, nums, k):

        left = 0
        right = k

        Sums = []
        current = 0

        while right <= len(nums):

            for i in range(k):
                if nums[i + left] > current:
                    current = nums[i + left]

                print(current)

            Sums.append(current)
            current = 0

            left += 1
            right += 1

        return Sums





