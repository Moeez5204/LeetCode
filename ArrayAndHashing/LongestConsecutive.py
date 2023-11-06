class Solution(object):
    def longestConsecutive(self, num):
        """
        :type nums: List[int]
        :rtype: int


        order the list 
        add the first number to dictionary 
        keep going till the next number is not there 
        next key in dictionary 
        repeat till nums is finished 

        """

        num = sorted(num)
        Longest, Current = 0, 1
        Checked = False

        if len(num) == 0:
            return 0

        if len(num) == 1:
            return 1

        for i in range(0, len(num) - 1):
            print(num[i + 1], num[i] + 1)
            if num[i + 1] == num[i] + 1:
                Current += 1

            else:
                if Current > Longest:
                    Longest, Current = Current, 0
                Checked = True

        if Longest > Current:
            return Longest
        else:
            return Current + 1






