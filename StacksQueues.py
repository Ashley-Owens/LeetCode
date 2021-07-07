# CodePath Advanced Interview Prep Course
# LeetCode Stack & Queue Practice Problems
# 8/29/2020
# 7/07/2021

# UMPIRE: 
# Understand the problem, 
# Match the problem to one or more data structures, 
# Pseudocode,
# Implement in code, 
# Recheck/Reflect, 
# Evaluate your solution's time and space complexity


# Stack Problem Solving Options
# 1. Useful for adding/removing in particular orders i.e. most recent element

# Queue Problem Solving Options
# 1. Useful for ordering elements in FIFO order


def postfix(string):
    """
    Write a function to evaluate the value of an expression in postfix notation represented by a string with numbers between 0 and 9 and operators separated by whitespace. The expression supports 4 binary operators '+', '*', '-' and '/'.
    Args:
        string (str): string of integers and operators
    Returns:
        int/float: calculation of string
    """
    # If string is empty return 0
    if string == "":
        return 0

    # Initialize a stack variable using python library or list[]
    stack = []

    # Initialize a set of operators
    operators = {
        '+' : lambda a, b: a + b,
        '*' : lambda a, b: a * b,
        '-' : lambda a, b: a - b,
        '/' : lambda a, b: a / b
    }

    for char in string:

        if char.isdigit():
            stack.append(int(char))

        if char in "+-*/":
            # Pop previous two elements from the stack
            b = stack.pop() # b is the top element in the stack
            a = stack.pop() # a is two elements from the top of the stack
            calculation = operators[char]

            # Perform operation and add to stack
            stack.append(calculation(a, b))

    return stack.pop()


# Output: 14
print(postfix("5 1 2  +  4  * +  3  -"))

