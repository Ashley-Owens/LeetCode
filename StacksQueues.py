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

from queue import Queue


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


def isValid(s):
    dict = {')': '(', '}': '{', ']':'['}
    stack = []

    for char in s:
        
        if char not in dict:
            stack.append(char)
        
        elif char in dict:
            if stack:
                if stack.pop() != dict[char]:
                    return False
            else:
                return False
    
    return len(stack) == 0


def reverseFirstKElements(q, k):
    """Reverse first k elements of a queue. If k is greater than the
    number of elements in the input, return the original queue.

    Args:
        q (Queue): Python object filled with integers
        k (int): number of items to reverse

    Returns:
        Queue: Python object in proper order
    """
    size = q.qsize()
    stack = []
    
    if k > size or k <= 0:
        return q
    
    if not q:
        return q
    
    for i in range(k):
        stack.append(q.get())
        
    while stack:
        q.put(stack.pop())
        
    for _ in range(size - k):
        num = q.get()
        q.put(num)
    
    return q


# Output: 14
print(postfix("5 1 2  +  4  * +  3  -"))

# Output False
print(isValid('([)]'))
# Output: True
print(isValid('{[]}'))

# Input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and k=4
# Output [4, 3, 2, 1, 5, 6, 7, 8, 9, 10]
q = Queue(maxsize=10)
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in items:
    q.put(i)
# print(list(q.queue))
res = reverseFirstKElements(q, 4)
print(list(res.queue))
