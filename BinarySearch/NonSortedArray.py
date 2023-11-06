class Solution:
    def findMin(self, num):
        left, right = 0, len(num) - 1
        while left < right:
            midpoint = (left + right) // 2
            if num[midpoint] > num[right]:
	            left = midpoint + 1
            else:
                right = midpoint
        return num[left]
