class Solution(object):
    def searchMatrix(self, matrix, target):
        List = sorted([item for sublist in matrix for item in sublist])
        return True if target in List else False