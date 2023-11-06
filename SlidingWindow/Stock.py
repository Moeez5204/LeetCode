class Solution(object):
    def maxProfit(self, Prices):
        Front, End = 0, 1
        MaxProfit = 0

        while End < len(Prices):
            Current = Prices[End] - Prices[Front]

            if Prices[Front] < Prices[End]:
                MaxProfit = max(Current, MaxProfit)
            else:
                Front = End
            End += 1

        return MaxProfit

