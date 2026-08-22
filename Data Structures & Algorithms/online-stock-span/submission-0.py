class StockSpanner:

    def __init__(self):
        self.p = []

    def next(self, price: int) -> int:
        self.p.append(price)
        old = self.p[-1]
        i = len(self.p)-2
        c=1
        while i>=0:
            if self.p[i]<=old:
                c+=1
            else:
                break 
            i-=1
        return c 
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)