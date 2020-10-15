def cutRod(prices, n, cost):
    """
    Consider a modification of the rod-cutting problem in which, in addition to a price pi for each rod, each cut incurs a fixed cost of c. The revenue associated with a solution is now the sum of the prices of the pieces minus the costs of making the cuts. Give a dynamic-programming algorithm to solve this modified problem.

    Args:
        prices (array): an array filled with rod prices
        n (int): length of prices array
        cost (int): cost to be deducted for cuts

    Returns:
        int: the maximum value 
    """
    val = [0] * (n+1)
    
    for j in range(1, n + 1):
        val[j] = prices[j-1]
        
        for i in range(j):
            val[j] = max(val[j], prices[i] + val[j - i-1] - cost)

    return val[n]
    
    
    
# arr = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30] 
# size = len(arr) 
# print("Maximum Obtainable Value is " + str(cutRod(arr, size, 1))) 




def makeChange(V, A):
    """
    Making Change: Given coins of denominations (value) 1 = v1 < v2 < ... < vn, we wish to make change for an amount A using as few coins as possible. Assume that vi’s and A are integers. Since v1= 1 there will always be a solution. Formally, an algorithm for this problem should take as input an array V where V[i] is the value of the coin of the ith denomination and a value A which is the amount of change we are asked to make. The algorithm should return an array C where C[i] is the number of coins of value V[i] to return as change and m the minimum number of coins it took. You must return exact change with the minimum number of coins.
    Args:
        V (list): an array of coin denominations
        A (int): the target number to make change for
    Returns:
        list: an array of the number of minimum coins required for each denomination to make change for A.
    """
    
    table = [[0 for i in range(A+1)] for j in range(len(V))]
    C = [0] * len(V) 
      
    # Initializes matrix, storing minimum coins required for each row (V[i]).
    for i in range(len(V)): 
        
      
      # Columns: total number of subproblems or A
        for j in range(A+1):
        
            # Populates first column with zeros
            if j == 0:
                table[i][j] = 0
            
            # Populates first row with 0 – len(A) since V[0] equals 1.
            elif V[i] == 1:
                table[i][j] = j
    
            else:
                # The coin denomination is too large, so just take the previously determined least coinage.
                if V[i] > j:
                    table[i][j] = table[i-1][j]
                 
                # Calculates min coins based on current and previous values
                else:
                    target = j - V[i]
                    minCoins = table[i][target] +1
    
                    # Need to determine if current minimum number of coins is less than previously found value.
                    if table[i-1][j] < minCoins:
                        table[i][j] = table[i-1][j]
                    else:
                        table[i][j] = minCoins
    print(table)
    # Populates C array with the minimum coins for each V[i].
    i = len(V)-1
    j = A
    minCoins = table[i][j]

    while j > 0:
    
        if table[i-1][j] > minCoins:
            j = j - V[i]
            C[i] += 1
            minCoins = table[i][j]
        
        else:
            i -= 1
             
    return C
    
A = 20
V = [1, 5]

print(makeChange(V, A))