class Solution(object):
    def isPalindrome(self, s):

        Back, Front = 0, len(s) - 1
        while Back < Front:
            while Back < Front and not s[Back].isalnum():
                Back += 1
            while Back < Front and not s[Front].isalnum():
                Front -= 1

            if s[Back].lower() != s[Front].lower():
                return False

            Back, Front = Back + 1, Front - 1

        return True