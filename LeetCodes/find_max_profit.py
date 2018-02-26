"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Example 1:

Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

Example 2:

Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

"""

#YOUR CODE GOES HERE
def max_profit_helper(price):
    """
    Input: array with stock prices
    output: profit gained by selling stock from one transcation
    
    Start with finding the lowest stock price ith index
    Then find the maximum stock price that is > ith index
    Subtract the two
    
    """
    max_out = 0
    min_index = 0
    for i in range(1,len(price)):
        if price[i] < price[min_index]:
            min_index = i
    for j in range(min_index,len(price)):
        diff = price[j] - price[min_index]
        if (price[j]>price[min_index]) and (diff > max_out):
            max_out = diff
    
    return max_out


##DON"T CHANGE THIS
def max_profit(price):
    return max_profit_helper(price)

#test case
def main():
    price = [7, 1, 5, 3, 6, 4]
    print ("Test Case 1:")
    print ("Expected result: 5")
    print ("Your result is: {}".format(max_profit(price)))
    price = [7, 6, 4, 3, 1]
    print ("Test Case 2:")
    print ("Expected result: 0")
    print ("Your result is: {}".format(max_profit(price)))

if __name__ == "__main__":
    main()