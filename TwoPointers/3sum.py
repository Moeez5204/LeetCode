class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums = sorted(nums)
        result = []

        for i in range(len(nums) - 2):  # two pointers

            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip dupes

            left, right = i + 1, len(nums) - 1

            while left < right:

                _sum = nums[i] + nums[left] + nums[right]

                if _sum == 0:  # add triplets to results
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # skips dupes

                    left += 1  # next iterato
                    right -= 1

                elif _sum < 0:
                    left += 1

                else:
                    right -= 1

        return result





