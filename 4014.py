class Solution(object):
    def minPrice(self, prices, discounts):
        prices.sort(reverse = True)
        discounts.sort(reverse = True)
        total = 0.00

        for i in range(min(len(prices), len(discounts))):
            price = prices[i]
            discount = discounts[i]

            total = total + ((price * (100.00 - discount)) / 100)

        for i in range(len(discounts),len(prices)):
                    total = total + prices[i]

        return total        
