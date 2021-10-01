# CodePath Intermediate Interview Prep Course
# LeetCode Binary Tree Practice Problems
# 8/7/2021

# UMPIRE: 
# Understand the problem
# Match the problem to one or more data structures
# Pseudocode
# Implement in code
# Recheck/Reflect
# Evaluate your solution's time and space complexity


# Binary Tree Problem Solving Options

#  Breadth First Search (queue)
#       1. Level-order Traversal

#  Depth First Search (stack)
#       1. Pre-order Traversal
#       2. Post-order Traversal: good for iterating all subtrees first
#       3. In-order Traversal

#  Can use either Recursion or Iteration + Data Structure
#       - Recursion Space Complexity: typically O(height)
#       - Recursion Time Complexity: typically O(n) if visiting every node

# Using an array
# node = Index
# left = index *2 + 1
# right = index *2 + 2
# Recursive solutions: include space complexity on the stack O(h)
# Talk about how time complexity is affected by balanced O(log n) vs unbalanced tree O(n)
#  ** Make sure you understand what the problem will return **
#  ** List out possible traversals **
#  ** Have explicit pseudocode **
#  ** Think iteratively first **
#  ** Don't say: I don't Know **

"""
Tree Traversal Notes

Pre-Order:
-> Visit Node
-> Recurse Left
-> Recurse Right

In-Order:
-> Recurse Left
-> Visit Node
-> Recurse Right

Post-Order:
-> Recurse Left
-> Recurse Right
-> Visit Node

Level-Order:
-> Recurse Left to Right
"""


class TreeNode:
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, node):
        """
        Given the root of a binary tree, return all root-to-leaf paths in any order.
        Uses pre-order traversal to print every root to leaf path

        Args:
            node (object): TreeNode
            lst (list, optional): holds values of visited nodes along path. Defaults to [].
        """
        if not node:
            return []
        
        if not node.left and not node.right:
            return [str(node.val)]

        leftPathToLeaf = self.binaryTreePaths(node.left) 
        rightPathToLeaf = self.binaryTreePaths(node.right)
        
        left = [str(node.val)+ ("->"+lpath ) for lpath in leftPathToLeaf]
        right = [str(node.val)+ ("->"+rpath) for rpath in rightPathToLeaf]
        return left+right

    def doubleTree(self, root):
        """
        For each node in a binary tree, create a new duplicate node, and
        insert the duplicate as the left child of the original node. Uses
        postorder traversal.
        Args:
            root (object): TreeNode
        Returns:
            root: TreeNode
        """
        if not root:
            return
        
        next_node = root
        self.doubleTree(root.left)
        self.doubleTree(root.right)
        
        next_node = root.left
        root.left = TreeNode(root.val)
        root.left.left = next_node
        return root

    def sortedArrayToBST(self, nums):
        """
        Given an integer array nums where the elements are sorted in ascending order,
        convert it to a height-balanced binary search tree. A height-balanced binary tree 
        is a binary tree in which the depth of the two subtrees of every node never differs
        by more than one.
        Args:
            nums (list): list of integers in ascending order
        Returns:
            object: TreeNode
        """
        return self.buildSubTree(nums, 0, len(nums) - 1)

    def buildSubTree(self, nums, start, end):
        """
        Recursive helper method for sortedArrayToBST
        Args:
            nums (int): list of nums to convert to BST
            start (int): index position
            end (int): ending list index position
        Returns:
            object: TreeNode
        """
        # Base case 
        if start > end:
            return None

        # Find middle Index
        middle = (end + start) // 2 

        root = TreeNode(nums[middle])  
        root.left = self.buildSubTree(nums, start, middle - 1) 
        root.right = self.buildSubTree(nums, middle + 1, end)

        return root

def printTree(root):
    if not root:
        return

    if root:
        print(root.val)
    printTree(root.left)
    printTree(root.right)


# Tests for binaryTreePaths
tree = TreeNode(1)
tree2 = TreeNode(2)
tree3 = TreeNode(3)
tree.left = tree2
tree.right = tree3
sol = Solution()
print(sol.binaryTreePaths(tree))

# Tests for doubleTree
tree = TreeNode(1)
tree2 = TreeNode(2)
tree3 = TreeNode(3)
tree.left = tree2
tree.right = tree3
# print(sol.doubleTree(tree))

# Tests for sortedArrayToBST
nums = [-10,-3,0,5,9]
tree = sol.sortedArrayToBST(nums)
# printTree(tree)
