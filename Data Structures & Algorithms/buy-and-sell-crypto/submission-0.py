class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy = prices[0]
        max_profit=0

        for price in prices:
            if best_buy > price: #Getting the minor value for buying
                best_buy = price
            if price - best_buy > max_profit:
                max_profit = price - best_buy
        return max_profit

        #i must pick the lower first value and the bigger last_value
        #Input: prices = [10,1,5,6,7,1]
        #best_buy=0
        #best_sell=?
        #max_profit=0
        #Output: 6
        #best_buy as the minor value:
            #if price[i] < best_buy
                #best_buy = price[i]
            # price[i] - best_buy > max_profit:
                # max_profit = price[i] - best_buy