def max_profit(array):

    max_profit = 0

    for i in range(len(array)):
        buy_value = array[i]
        for j in range(i, len(array)):
            if array[j] - buy_value > max_profit:
                max_profit = array[j] - buy_value

    return max_profit



def max_profit_optimized(prices):
    min_price = float('inf')    # represents positive infinity
    best = 0

    for p in prices:
        if p < min_price:
            min_price = p
        else:
            best = max(best, p - min_price)
    
    return best