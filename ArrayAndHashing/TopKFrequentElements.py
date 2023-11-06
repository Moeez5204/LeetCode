from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        counter = Counter(nums).most_common(k)
        values = [item[0] for item in counter]
        return values