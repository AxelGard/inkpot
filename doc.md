| def | doc-str |
| --- | --- |
|     __init__(self, symbolstr) |self.symbol = symbol|
|     price(self) -> float  # PREV current_price | returns the current price of given symbol (str) |
|     value(self) -> float  # prev value_of_stock | takes a string sym. Gets and returns the stock value at close |
|     buy(self, qty int) | buys a stock. Takes int qty and a string sym |
|     sell(self, qty int) | sells a stock. Takes int qty and a string sym|
|     order(self, qty int, beh str) -> float | submit order and is a template for order |
|     is_shortable(self) -> bool | checks if stock can be shorted |
|     can_borrow(self) -> bool |check whether the name is currently|
|     barset(self, limitint) | returns barset for stock for time period lim |
|     historical_data(self, nr_days=1000) |returns a list of the stocks closing value,|
|     week_pl_change(self) | Percentage change over a week |
|     is_tradable(self) | return if the stock can be traded|
|     position(self) | returns position of stock |
|     today_plpc(self) | stock today's profit/loss percent |
|     plpc(self) | stock sym (str) Unrealized profit/loss percentage |
|     exchange_is_open(self) -> bool | returns if exchange is open |
|     __repr__(self) |return f"{self.symbol}@(${self.price})"|
|     __str__(self) |return f"{self.symbol}"|
|     __eq__(self, other) |if isinstance(other,(int,float)):|
|     __ne__(self, other) |if isinstance(other,(int,float)):|
|     __lt__(self, other) |if isinstance(other,(int,float)):|
|     __le__(self, other) |if isinstance(other,(int,float)):|
|     __gt__(self, other) |if isinstance(other,(int,float)):|
|     __ge__(self, other) |if isinstance(other,(int,float)):|
|     __add__(self, other) |if isinstance(other,(int,float)):|
|     __radd__(self, other) |return self.price + other|
|     __sub__(self, other) |if isinstance(other,(int,float)):|
|     __rsub__(self, other) |return self.price - other|
|     __mul__(self, other) |if isinstance(other,(int,float)):|
|     __rmul__(self, other) |return self.price * other|
|     __truediv__(self, other) |if isinstance(other,(int,float)):|
|     __rdiv__(self, other) |return self.price / other|
|     __floordiv__(self, other) |if isinstance(other,(int,float)):|
|     __rfloordiv__(self, other) |return self.price // other|
|     __abs__(self) |# dose not rely makes sense should not be able to|
|     __int__(self) |return int(self.price)|
|     __float__(self) |return float(self.price)|
|     __round__(self, nDigits) |return round(self.price, nDigits)|
