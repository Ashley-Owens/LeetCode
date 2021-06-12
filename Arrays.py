# CodePath Advanced Interview Prep Course
# LeetCode List/Array Practice Problems
# 9/7/2020
# 6/12/2021

# UMPIRE: Understand the problem, Match the problem to one or more data structures, write Pseudocode,
# Implement in code, Recheck/Reflect, Evaluate your solution's time and space complexity.

# Array Problem Solving Options
# 1. Sort the array and determine which direction to loop, forward or reverse.
# 2. Two-Pointer: fast & slow pointer or index 0 & len(list)-1 pointer for comparisons
#    during list iteration.
# 3. Second array: use a second array to store values.


class Solution:

    def moviesOnFlight(self, d, movieDuration):
        """
        Find the pair of movies with the longest total duration that is less than or equal
        to (d - 30min). If multiple found, return the pair with the longest total runtime.
        Args:
            d (int): flight duration in minutes
            movieDuration (list): list of integer movie durations in minutes        
        Returns:
            list: list containing a pair of movie durations
        """
        result, d = [], d - 30
        movieDuration.sort(reverse = True)
        
        # Edge cases will return an empty list.
        if d <= 0 or not movieDuration:
            return []
          
        for i in range(0, len(movieDuration) - 2):

            # First pointer tracked.
            curr = [movieDuration[i]]

            # Second pointer iterates through remainder of array.
            for j in range(i + 1, len(movieDuration)):
                if curr[0] + movieDuration[j] <= d:  
                    curr.append(movieDuration[j])
                    break
            
            # Updates result with the largest pair.
            if sum(result) < sum(curr):
                result = curr.copy()

        return result

    def cellCompete(self, states, days):
        """
        Each day, for each cell, if its neighbours are both active or both inactive, the cell 
        becomes inactive the next day, otherwise it becomes active the next day. The two cells on
        the ends have single adjacent cell, so the other adjacent cell is assumed to be always inactive.   
        Args:
            states (list): array of 0's and 1's representing active/inactive cells
            days (int): number of days to update the array
        Returns:
            list: an updated array of active/inactive cells
        """
        temp = states[:]
        n = len(states)
        
        # Uses bitwise XOR operator to update cells
        while days > 0:

            # Updates the cells on each end.
            temp[0] = False ^ states[1]
            temp[n-1] = False ^ states[n-2]
            
            # Updates the inner cells.
            for i in range(1, n-1):
                temp[i] = states[i-1] ^ states[i+1]
            
            states = temp[:]
            days -= 1
        
        return states

    def generalizedGCD(self, num, arr):
        """
        Iterates through an array and finds the GCD between two numbers using a helper method.
        Args:
            num (int): length of array
            arr (list): list of integers
        Returns:
            int: the greatest common divisor
        """
        n1 = arr[0]
        n2 = arr[1]
        gcd = self.findGCD(n1, n2)
        
        for i in range(2, num):
            gcd = self.findGCD(gcd, arr[i])
            
        return gcd
    
    
    def findGCD(self, n1, n2):
        """
        Helper method implements the Euclidian algorithm to find H.C.F. of two numbers. 
        Args:
            n1 (int): first number
            n2 (int): second number
        Returns:
            int: the great common divisor of two numbers
        """
        while n2:
            n1, n2 = n2, n1 % n2
        
        return n1

    def numPlayers(self, cutOffRank, num, scores):
        if not scores:
            return 0

        count = 0
        pos = 1
        ranks = []
        scores.sort(reverse=True)
        
        for i, j in enumerate(scores):
            
            if j == 0:
                ranks.append(None)
            
            elif i == 0:
                ranks.append(pos)
            
            elif j == scores[i-1]:
                ranks.append(pos)

            else:
                pos += 1
                ranks.append(pos)
        
        for pos in ranks:
            if pos == None:
                continue
            if pos <= cutOffRank:
                count += 1
        
        print(ranks)
        return count

    def chooseFlask(self, numOrders, requirements, flaskTypes, totalMarks, markings):

        losses, flaskOptions = 0, []
        for i in range(numOrders):
        
            for j in range(totalMarks):
        
                if markings[j] in flaskOptions:
                    if markings[j][1] < requirements[i]:
                        flaskOptions.remove(markings[j])
                        
                elif markings[j][1] >= requirements[i]:
                    flaskOptions.append(markings[j])
        
        print(flaskOptions)
        flaskOptions.sort()

        return flaskOptions[0] 

    def longest_subsequence(self, arr):
        """
        Longest Consecutive Subsequence: Given an unsorted array of integers, 
        we want to find the length of the longest subsequence such that elements 
        in the subsequence are consecutive integers. The consecutive numbers can 
        be in any order.
        Args:
            arr (list): list of integers
        Returns:
            int: length of the longest subsequence
        """
        # Edge cases
        if len(arr) <= 1:
            return len(arr)

        # Sort the array O(n log(n))
        arr.sort()
        curr = 0
        longest = 0
        
        # Loop through the array O(n)
        for i in range(len(arr)):
            if arr[i] == arr[i-1]:
                continue
            
            elif arr[i] - arr[i-1] == 1:
                curr += 1
                        
            else:
                longest = max(curr, longest)
                curr = 1
        
        # O(n log(n)) time and O(1) space complexity
        return longest



if __name__ == "__main__":
    
    sol = Solution()

    # # Tests moviesOnFlight method
    # print(sol.moviesOnFlight(250, [90, 85, 75, 60, 120, 150, 125]))
    # print(sol.moviesOnFlight(25, [90, 85, 75, 60, 120, 150, 125]))
    # print(sol.moviesOnFlight(250, [0]))

    
    # # Tests generalizedGCD
    # print(sol.generalizedGCD(5, [2, 3, 4, 5, 6]))
    # print(sol.generalizedGCD(5, [2, 4, 6, 8, 10]))

    # # Tests cellCompete method
    # print(sol.cellCompete([1, 0, 0, 0, 0, 1, 0, 0], 1))
    # # Answer = [0, 1, 0, 0, 1, 0, 1, 0]
    # print(sol.cellCompete([1, 1, 1, 0, 1, 1, 1, 1], 2))
    # # Answer = [0, 0, 0, 0, 0, 1, 1, 0]


    # print(sol.numPlayers(0, 4, [0, 0, 0, 0]))

    # print(sol.chooseFlask(4, [4, 6, 6, 7], 3, 9, [[0, 3], [0, 5], [0, 7], [1, 6], [1, 8], [1, 9], [2, 3], [2, 5], [2, 6]]))

    # print(sol.longest_subsequence([36, 41, 56, 35, 44, 33, 34, 43, 92, 32, 42]))
    # solution = 5