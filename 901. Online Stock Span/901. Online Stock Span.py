class StockSpanner:
    
    def __init__(self):
        self.prices = []

    def next(self, price):
        w = 1
        while self.prices and self.prices[-1][0] <= price:
            w += self.prices[-1][1]
            self.prices.pop()
            
        self.prices.append([price, w])
        return w

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)