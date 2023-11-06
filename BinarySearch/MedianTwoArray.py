class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        for i in range(len(nums2)):
            nums1.append(nums2[i])

        sortedList = sorted(nums1)
        print(sortedList)


        left, right = 0, len(sortedList) - 1

        while True:
            if left == right:
                return sortedList[left]

            elif left + 1 == right:
                median = (sortedList[left] + sortedList[right])
                return float(median) / 2

            else:
                left, right = left + 1, right - 1





