class Solution(object):
    def lastStoneWeight(self, stones):
        stones.sort()
        while len(stones) != 1:
            stones[-2] = stones[-1] - stones[-2]
            stones.pop(len(stones) - 1)
            stones.sort()
        return stones[-1]


