def cutRod(prices, n, cost):
    """
    Consider a modification of the rod-cutting problem in which, in addition to a price pi for each rod, each cut incurs a fixed cost of c. The revenue associated with a solution is now the sum of the prices of the pieces minus the costs of making the cuts. Give a dynamic-programming algorithm to solve this modified problem.

    Args:
        prices (array): an array filled with rod prices
        n (int): length of prices array
        cost (int): cost to be deducted for cuts

    Returns:
        [type]: [description]
    """
    val = [0] * (n+1)
    
    for j in range(1, n + 1):
        val[j] = prices[j-1]
        
        for i in range(j):
            val[j] = max(val[j], prices[i] + val[j - i-1] - cost)

    return val[n]
    
    
    
arr = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30] 
size = len(arr) 
print("Maximum Obtainable Value is " + str(cutRod(arr, size, 1))) 