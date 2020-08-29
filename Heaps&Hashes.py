# CodePath Advanced Interview Prep Course
# LeetCode Hash Table and Heap Practice Problems
# 8/21/2020

# UMPIRE: Understand the problem, Match the problem to one or more data structures, write Pseudocode,
# Implement in code, Recheck/Reflect, Evaluate your solution's time and space complexity.

# Hash Table Problem Solving Options
# 1. Use for quick access to keys or values

# Heap Problem Solving Options
# 1. Use when you only need the top most/least frequent occurrences

import heapq

class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Determines if two strings are isomorphic. All occurrences of a character must 
        be replaced with another character while preserving the order of characters. No
        two characters may map to the same character but a character may map to itself.
        Args:
            s (str): string
            t (str): string
        Returns:
            bool: True if isomorphic, else False
        """
        # Initializes dictionaries for storing string values.
        d1, d2 = {}, {}

        # Maps each string to a value. 
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]

        # Sorts the values of each dictionary, comparing the results.
        return sorted(d1.values()) == sorted(d2.values())

    def isHappy(self, n: int) -> bool:
        """
        Starting with any positive integer, replace the number by the sum of the squares of its digits, 
        and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in 
        a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
        Args:
            n (int): starting integer
        Returns:
            bool: True if n is a happy number, else False
        """
        # Creates a set for tracking numbers that have been encountered.
        seen = set()

        while n not in seen:
            seen.add(n)
            n = sum(int(x) **2 for x in str(n))
        
        return n == 1

    def topKFrequent(self, words, k: int):
        """
        Given a non-empty list of words, return the k most frequent elements. Sort answer by frequency 
        from highest to lowest. If two words have the same frequency, then the word with the lower 
        alphabetical order comes first.
        Args:
            words (list): list of lowercase letters
            k (int): 1 ≤ k ≤ number of unique elements
        Returns:
            list(str): alphabetized list
        """
        # Creates dictionary for storing words mapped to frequencies
        d1, result, word_count_pairs = {}, [], []

        # Populates dictionary with words: frequency.
        for item in words:
            d1[item] = d1.get(item, 0) +1

        # Adds tuple pairing of count: word data to a list.
        for word, count in d1.items():

            # Uses negative count due to Python Min Heap DS and we need max heap values.
            word_count_pairs.append((-count, word))
        
        # Adds count: word pairings to a min heap data structure.
        heapq.heapify(word_count_pairs)
        for _ in range(k):

            # Grabs only the word in the pairs tuple.
            result.append(heapq.heappop(word_count_pairs)[1])

        return result

    def kSmallestPairs(self, nums1, nums2, k: int):
        """
        Define a pair of values which consists of one element from each array. Find the k pairs
        with the smallest sums. Visualize input as a nums1 x nums2 matrix of sums. We just need
        the sums in the top leftmost area of the matrix.
        Args:
            nums1 (list): sorted integer array
            nums2 (list): sorted integer array
            k (int): number of pairs to return
        Returns:
            list: a list of lists with the smallest pairs from each array
        """
        # Edge case for an empty list.
        if not nums1 or not nums2:
            return []

        # Both lists are sorted, thus start by storing the sum of the smallest 
        # elements and each element's starting index.
        heap = [(nums1[0] + nums2[0], 0, 0)]

        # Stores the smallest pair combinations from both lists.
        pairs = []

        def push(i, j):
            """Adds indices to the heap."""
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(heap, [nums1[i]+nums2[j], i, j])

        # Continues looping until reaching k pairs or running out of heap elements.
        while len(pairs) < k and heap:

            # '_' contains the sum of two list elements followed by their indices i and j i.e. (7, 0, 2)
            _, i, j = heapq.heappop(heap)

            # Adds a tuple of smallest values to the result using the indices from sorted heap DS.
            pairs.append([nums1[i], nums2[j]])

            # Adds current sum of elements with their indices to the heap.
            push(i, j+1)

            # We only need elements from the top leftmost aspect of the matrix.
            if j == 0:
                push(i+1, j)

        return pairs

if __name__ == "__main__":
    
    sol = Solution()
    
    # # Tests isIsomorphic method
    # print(sol.isIsomorphic("foo", "bar"))
    # print(sol.isIsomorphic("paper", "title"))


    # # Tests isHappy method
    # print(sol.isHappy(2))
    # print(sol.isHappy(19))

    # # Tests topKFrequent Words Method
    # print(sol.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], k = 2))
    # print(sol.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4))
    # print(sol.topKFrequent(["dog", "cat", "monkey", "dog", "cat", "monkey"], k = 2))

    # # Tests kSmallestPairs method
    # print(sol.kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3))
    # print(sol.kSmallestPairs(nums1 = [1,1,2], nums2 = [1,2,3], k = 2))
    # print(sol.kSmallestPairs(nums1 = [1,2], nums2 = [3], k = 3))
    # print(sol.kSmallestPairs(nums1 = [2, 4, 6], nums2 = [1, 3, 5], k = 3))
