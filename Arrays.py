# CodePath Advanced Interview Prep Course
# LeetCode List/Array Practice Problems
# 9/7/2020

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
        the ends have single adjacent cell, so the other adjacent cell is assumsed to be always inactive.   
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
            temp[0] = False ^ states[1]
            temp[n-1] = False ^ states[n-2]
            
            for i in range(1, n-1):
                temp[i] = states[i-1] ^ states[i+1]
            
            states = temp[:]
            days -= 1
        
        return states
        

    def generalizedGCD(self, num, arr):
    # WRITE YOUR CODE HERE
    
        n1 = arr[0]
        n2 = arr[1]
        gcd = self.findGCD(n1, n2)
        
        for i in range(2, num):
            gcd = self.findGCD(gcd, arr[i])
            
        return gcd
    
    
    def findGCD(self, n1, n2):
        while n2:
            n1, n2 = n2, n1 % n2
        
        return n1


if __name__ == "__main__":
    
    sol = Solution()

    # # Tests moviesOnFlight method
    # print(sol.moviesOnFlight(250, [90, 85, 75, 60, 120, 150, 125]))
    # print(sol.moviesOnFlight(25, [90, 85, 75, 60, 120, 150, 125]))
    # print(sol.moviesOnFlight(250, [0]))

    
    # # Tests generalizedGCD
    # print(sol.generalizedGCD(5, [2, 3, 4, 5, 6]))
    # print(sol.generalizedGCD(5, [2, 4, 6, 8, 10]))

    print(sol.cellCompete([1, 0, 0, 0, 0, 1, 0, 0], 1))
    # Answer = [0, 1, 0, 0, 1, 0, 1, 0]
    print(sol.cellCompete([1, 1, 1, 0, 1, 1, 1, 1], 2))
    # Answer = [0, 0, 0, 0, 0, 1, 1, 0]
