class Purchase:

    def __init__(self, price_map: List[int], purchase_date: int):
        if purchase_date < 0 or len(price_map) < purchase_date:
            raise ValueError(f"Invalid purchase date, must be between 0 and {len(price_map)}: {purchase_date}")
        self.price_map = price_map
        self.purchase_info = purchase_date, self.price_map[purchase_date], 0
        self.best_sale_info = self._get_best_sale_data()

    @property
    def purchase_date(self):
        return self.purchase_info[0]

    @property
    def purchase_price(self):
        return self.purchase_info[1]
    
    @property
    def max_profit(self):
        return self.best_sale_info[2]
    
    def profit(self, sale_date: int|None = None) -> int:
        if sale_date is None:
            return 0
        return self.price_map[sale_date] - self.price_map[self.purchase_date]

    def _get_best_sale_data(self) -> int|None:
        max_future_price = max(self.price_map[self.purchase_date:])
        if max_future_price > self.purchase_price:
            date = self.price_map[self.purchase_date:].index(max_future_price) + self.purchase_date
            return date, self.price_map[date], self.profit(date)
        return None, self.price_map[self.purchase_date], 0

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_purchase = None
        for x, x_val in enumerate(prices):
            purchase = Purchase(prices, x)
            # print(f"Purchase Info: {purchase.purchase_info}, Sale Info: {purchase.best_sale_info}")
            if best_purchase is None:
                best_purchase = purchase
            if best_purchase.max_profit < purchase.max_profit:
                best_purchase = purchase 
        return best_purchase.max_profit
