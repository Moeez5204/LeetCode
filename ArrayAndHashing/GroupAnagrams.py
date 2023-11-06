class Solution(object):
    def groupAnagrams(self, strs):
        table = {}

        for strings in strs:
            String_Sorted = ''.join(sorted(strings))

            if String_Sorted not in table:
                table[String_Sorted] = []

            table[String_Sorted].append(strings)


        return list(table.values())