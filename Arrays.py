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
            curr = [movieDuration[i]]
            for j in range(i + 1, len(movieDuration) - 1):
                if curr[0] + movieDuration[j] <= d:  
                    curr.append(movieDuration[j])
                    break
            if sum(result) < sum(curr):
                result = curr.copy()
        return result



if __name__ == "__main__":
    
    sol = Solution()

    # Tests moviesOnFlight method
    print(sol.moviesOnFlight(250, [90, 85, 75, 60, 120, 150, 125]))