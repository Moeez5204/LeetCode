class Solution(object):
    def lengthOfLongestSubstring(self, s):

        '''''

        Check array if letter is already in 
        if true then check if lenght is longer then max lenght 
        if not
        next item 



        '''''

        left, right = 0, 1
        MaxLenght = 0
        CurrentLenght = 0
        CurrentWord = []

        for i in range(len(s)):
            if s[i] not in CurrentWord:
                CurrentWord.append(s[i])
                CurrentLenght += 1
            else:
                if CurrentLenght > MaxLenght:
                    MaxLenght, CurrentLenght = CurrentLenght, 1
                for thing in range(len(CurrentWord) - 1):
                    CurrentWord.pop(thing)
        return MaxLenght






