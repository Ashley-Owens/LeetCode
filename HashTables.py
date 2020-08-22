# CodePath Advanced Interview Prep Course
# LeetCode Hash Table Practice Problems
# 8/21/2020

# Hash Table Problem Solving Options


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




if __name__ == "__main__":
    
    sol = Solution()
    
    # Tests isIsomorphic method
    print(sol.isIsomorphic("foo", "bar"))
    print(sol.isIsomorphic("paper", "title"))

