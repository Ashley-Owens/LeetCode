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

    def getMaxSum(self, arr, k):
        """
        Given an array of positive nums and a positive num 'k',
        find the maximum sum of any subarray of size 'k'.
        Args:
            arr ([array]): an array of positive integers
            k (int): positive integer
        Returns:
            int: the maximum sum of of the subarray size 'k'
        """
        if k > len(arr) or k == 0:
            return -1

        max_sum = 0

        for i in range(k):
            max_sum += arr[i]

        curr_sum = max_sum

        for i in range(k, len(arr)):
            curr_sum += arr[i] - arr[i-k]
            max_sum = max(curr_sum, max_sum)

        return max_sum

    def mergeArrays(self, nums1, nums2):
        # Write your code here
        nums1_ptr = len(nums1) -1

        # Add nums2 to nums1 array
        for n in nums2:
            nums1[nums1_ptr] = n
            nums1_ptr -= 1

        # Implement sort
        nums1 = self.quick_sort(nums1, 0, len(nums1) -1)
        return nums1

    def quick_sort(self, arr, start, end):
        if start < end:
            p = self.partition(arr, start, end)
            self.quick_sort(arr, start, p - 1)
            self.quick_sort(arr, p + 1, end)

    def partition(self, arr, start, end):
        pivot_index = start
        pivot = arr[pivot_index]

        while start < end:
            while start < len(arr) and arr[start] <= pivot:
                start += 1

            while arr[end] > pivot:
                end -= 1

            if start < end:
                arr[start], arr[end] = arr[end], arr[start]

        arr[end], arr[pivot_index] = arr[pivot_index], arr[end]

        return end


    def reverseWords(self, arr):
        """
        Write a method that takes a message as an array of characters 
        and reverses the order of the words in place.
        """
        if not arr:
            return ""

        # reverse the whole message first
        self.swapChars(arr, 0, len(arr) - 1)

        space_ptr = 0
        p1 = 0
        while space_ptr <= len(arr) - 1:
            while space_ptr <= len(arr) - 1 and arr[space_ptr] != ' ':
                space_ptr += 1

            # reverse each word
            self.swapChars(arr, p1, space_ptr - 1)
            space_ptr += 1
            p1 = space_ptr

        return "".join(arr)

    def swapChars(self, arr, p1, p2):
        """
        Helper method for reverseWords
        Args:
            arr (list): an array of chars
            p1 (int): pointer 1
            p2 (int): pointer 2
        """
        while p2 > p1:
            arr[p1], arr[p2] = arr[p2], arr[p1]
            p1 += 1
            p2 -= 1

    def simpleRateLimiter(self, maxRequests, window, requestTimestamps):
        """
        Given two integers maxRequests and window, and an array of integers requestTimestamps,
        implement a simple rate limiter for every request during the last window seconds if the number of
        prior requests has already reached the maxRequests limit, fail the request, otherwise - accept it. 
        As a result, return a boolean array - whether each request from requestTimeStamps has been accepted or not.
        All timestamps given in the array are given in seconds and the array is sorted in ascending order.
        Args:
            maxRequests (int): maximum allowable requests in given window
            window (int): number of seconds to allow maxRequests
            requestTimestamps (list): array of integers 
        Returns:
            list: array of boolean values 
        """
        if requestTimestamps:
            prev = requestTimestamps[0]
        output = []
        count = 0
        
        for i in range(len(requestTimestamps)):
            req = requestTimestamps[i]
            time_diff = req - prev
            count += 1
            
            # Case 1: prev counts don't matter since the time 
            # difference is larger than the rate limiting window
            if time_diff > window:
                count = 1
                output.append(True)
            
            # Case 2: if first case fails, we're within the time
            # limiting window and count needs to be less than maxRequest
            elif count > maxRequests:
                output.append(False)
                count = 0
            
            # Case 3: We're within time limiting window and within 
            # maxRequests for that window.
            else:
                output.append(True)
            
            # Set our previous value for comparisons
            prev = req
    
        return output


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

    # print(sol.getMaxSum([2,3,4,1,5], 2))
    # print(sol.getMaxSum([2, 1, 5, 1, 3, 2], 3))
    # print(sol.getMaxSum([1, 4, 2, 10, 2, 3, 1, 0, 20], 4))


    # print(sol.mergeArrays([1, 3, 7, 8, 15, 25, 0, 0, 0, 0], [-1, 4, 10, 11]))
    # print(sol.mergeArrays([1, 2, 3, 0, 0, 0], [2, 5, 6]))


    # Output: "steal pound cake"
    # words = ['c', 'a', 'k', 'e', ' ',
    #     'p', 'o', 'u', 'n', 'd', ' ',
    #     's', 't', 'e', 'a', 'l']
    # print(sol.reverseWords(words))

    
    print(sol.simpleRateLimiter(3, 5, [1, 1, 1, 2, 12, 32, 33, 34, 36]))
    # Output: [True, True, True, False, True, True, True, True, False]
    print(sol.simpleRateLimiter(3, 5, [1, 1, 1, 7, 13, 32, 33, 34, 36]))
    # Output: [True, True, True, True, True, True, True, True, False]
    print(sol.simpleRateLimiter(3, 5, []))
    # Output: []
