class Solution(object):
    def isValid(self, s):

        dicti = {'(': ')',
                 '{': '}',
                 '[': ']'
                 }

        Return = False

        K = [s[i] for i in range(len(s))]

        for i in range(len(K) / 2):

            key = K[i]
            value = dicti.get(key)

            if value != K[i + 1]:
                Return = False
            else:
                i += 1
                Return = True

        return Return


