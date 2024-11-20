# Best Time to Buy and Sell Stock. 121
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4

------------------------------------------------------------

Вам дан массив prices, где prices[i] — это цена акции в день i.
Вы хотите максимизировать свою прибыль, выбрав один день для покупки акции
и другой, более поздний день, для её продажи.

Верните максимальную прибыль, которую можно получить от этой транзакции.
Если прибыль получить невозможно, верните 0.

Пример 1:
Вход:
prices = [7, 1, 5, 3, 6, 4]
Выход:
5
Объяснение:
Купите в день 2 (цена = 1) и продайте в день 5 (цена = 6), прибыль = 6 - 1 = 5.
Учтите, что нельзя покупать в день 2 и продавать в день 1, так как покупка должна быть раньше продажи.

Пример 2:
Вход:
prices = [7, 6, 4, 3, 1]
Выход:
0
Объяснение:
В данном случае транзакции не выполняются, и максимальная прибыль = 0.

Ограничения:
1. 1 <= prices.length <= 10^5
2. 0 <= prices[i] <= 10^4
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) <= 2:
            return 0
        min_price = float('inf')  # Начальное значение для минимальной цены
        max_profit = 0  # Начальная прибыль
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))




