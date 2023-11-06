class Solution(object):
    def plusOne(self, digits):
        result = "".join(str(num) for num in digits)
        thing = int(result) + 1

        Array = [int(digit) for digit in str(thing)]
        return Array


