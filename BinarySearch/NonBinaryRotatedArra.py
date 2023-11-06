class Solution(object):
    def findMin(self, nums):
        """
        28ms
        """

        Sorted = list(sorted(nums))
        return Sorted[0]

