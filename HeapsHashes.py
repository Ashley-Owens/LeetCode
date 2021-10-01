# CodePath Advanced Interview Prep Course
# LeetCode Hash Table and Heap Practice Problems
# 8/21/2020

# UMPIRE: Understand the problem, Match the problem to one or more data structures, write Pseudocode,
# Implement in code, Recheck/Reflect, Evaluate your solution's time and space complexity.

# Hash Table Problem Solving Options
# 1. Use for quick access to keys or values. O(1) for lookup, insertion, and deletion, worst case is O(n) due to collisions.

# Heap Problem Solving Options
# 1. Use when you only need the top k most/least frequent occurrences and when fast lookup,
#    deletion, or searches don't matter.
# 2. Optimize building a heap by heapifying a list (O(n)) instead of inserting n times. 
#    Insertion and deletion are O(log n)


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

    def leastBricks(self, wall) -> int:
        """
        A brick wall is represented by a list of rows. Each row is a list of integers representing the width
        of each brick in this row from left to right. The bricks have the same height but different widths. Draw  
        a vertical line from the top to the bottom while crossing the least number of bricks.
        Args:
            wall (list): matrix of integers signifying width of each brick
        Returns:
            int: number of bricks crossed
        """
        # Stores the number of gaps at each index of a row.
        gaps = {}

        for row in wall:
            total = 0

            # A line can't be drawn at the wall's edges.
            for brick in row[:-1]:
                total += brick

                # Stores the row index: gap data in hash map.
                gaps[total] = gaps.get(total, 0) +1
        
        # Edge case for a wall with no gaps.
        if len(gaps) < 1:
            return len(wall)

        return len(wall) - max(gaps.values())

    def is_well_formed(self, string):
        """
        A string is well formed if for every "(" left parenthesis you have matching right one ")".
        In the same way every ")" should have a preceding "(". Runtime and space complexity is O(n).
        Args:
            string: a string comprised of any number/order of brackets
        Returns:
            bool: True if well formed, else False
        """
        unmatched_brackets = []
        bracket_pairings =  {"(": ")", "{": "}", "[": "]"}
        
        for char in string:
            if char in bracket_pairings:
                unmatched_brackets.append(char)

            # Edge case for incorrect chars.
            elif not unmatched_brackets: 
                return False

            # Implements stack ADT to determine matching brackets.
            elif bracket_pairings[unmatched_brackets.pop()] != char:
                return False

        return len(unmatched_brackets) == 0

    def arrayManipulation(self, n, queries):
        """
        Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array 
        element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array. 
        Args:
            n (int): length of the array of zeros
            queries (matrix):  integers a, b and k are the left index, right index and summand. 
        Returns:
            [type]: max array value after completing summations
        """
        # Brute force method using dictionaries, too slow.
        d = {}
        
        for lst in queries:
            for i in range(lst[0], lst[1]+1):
                d[i] = d.get(i, 0) + lst[2]
        return max(d.values())

        # Alternative method parses the input in the main function to obtain the 'm' value, 
        # which isn't provided to the actual function. See below.



    def sort_list(self, almost_sorted_list, m):
        """
        Given an almost sorted array in which each number is less than m spots away from its
        correctly sorted position, return a properly sorted array. Runtime is O(n log m).
        Args:
            almost_sorted_list (list): a list of almost sorted elements
            m (int): each item in the list is less than m spots away from proper location
        Returns:
            list: sorted array
        """
        min_heap, result = [], []

        for elem in almost_sorted_list[:m]:
            heapq.heappush(min_heap, elem)

        # In the second for loop, only add elements starting 
        # from the mth item in the almost sorted list.
        for elem in almost_sorted_list[m:]:
            heapq.heappush(min_heap, elem)
            result.append(heapq.heappop(min_heap))

        for i in range(len(min_heap)):
            result.append(heapq.heappop(min_heap))
            
        return result


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        """
        self.heap = []

        # Populates MH with initial values (if provided)
        if start_heap:
            for node in start_heap:
                self.insert(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return len(self.heap) == 0

    def insert(self, node: object) -> None:
        """
        Adds a new object to the MinHeap while maintaining min heap structure.
        Args:
            node (object): item to be added to the heap
        """
        # Saves the index position of the new node.
        position = len(self.heap)
        self.heap.append(node)

        # Percolates node upwards to maintain min heap structure.
        self.trickle_up(position)
    
    def trickle_up(self, position: int) -> None:
        """
        Recursively swaps nodes as needed to maintain min heap structure.
        Args:
            position (int): node index position in the heap
        """
        # Stops recursion at 0th index.
        if position == 0:
           return

        # Index position of parent node.
        j = (position - 1) // 2

        # Obtains values for comparison.
        parent = self.heap[j]
        node = self.heap[position]
        
        # Swaps nodes if needed to maintain min heap structure.
        if node < parent:
            self.heap[position], self.heap[j] = self.heap[j], self.heap[position]
            self.trickle_up(j)
        return


if __name__ == "__main__":
    
    sol = Solution()
    
    # # Creates a MinHeap
    # min_heap = MinHeap([10])
    # min_heap.insert(8)
    # min_heap.insert(5)
    # min_heap.insert(1)
    # min_heap.insert(6)
    # min_heap.insert(2)
    # print(min_heap)
    
    # # Tests isIsomorphic method
    print(sol.isIsomorphic("foo", "bar"))
    print(sol.isIsomorphic("paper", "title"))


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

    # # Tests leastBricks method
    # print(sol.leastBricks([[1, 2, 3], [1, 3, 2], [4, 1, 1]]))
    # print(sol.leastBricks([[3], [3], [3]]))
    # print(sol.leastBricks([[1,2,2,1], [3,1,2], [1,3,2], [2,4], [3,1,2], [1,3,1,1]]))

    # # Tests is_well_formed method
    # print(sol.is_well_formed("[()]"))
    # print(sol.is_well_formed("{)"))

    # # Tests sort_list method
    # print(sol.sort_list([3, 2, 1, 4, 6, 5], 3))

    # Tests Array Manipulation method.
    queries = [[1, 1, 0], [1, 2, 5], [3, 4, 100]]
    print(sol.arrayManipulation(3, queries))

    # # HackerRank alternate approach in the main() function
    # heap = []
    # # Parses file input from HackerRank
    # n, m = [int(v) for v in input().split()]

    # for _ in range(m):
    #     a, b, k = [int(v) for v in input().split()]
    #     heapq.heappush(heap, (a, +k))
    #     heapq.heappush(heap, (b+1, -k))

    # mr, cr = 0, 0
    # while len(heap) > 0:
    #     item = heapq.heappop(heap)
    #     cr += item[1]
    #     mr = max(mr, cr)
    