from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = len(prices) - 1
        mylist = []

        smallest_value = min(prices)
        print(smallest_value)