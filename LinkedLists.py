# CodePath Advanced Interview Prep Course
# LeetCode Linked List Practice Problems
# 8/17/2020

# Linked List Problem Solving Options
# 1. Sentinel head: useful if needing to return a list where changes might occur to head node (swapping, new list creation)
# 2. Pointer bookkeeping: placing indicators for the pointers you'll use to iterate the linked list.
# 3. Reverse: helpful for performing arithmetic on LL (addTwoNums) or checking for palindromes
# 4. Two-pointer: use for detecting cycles or intersections 
# 5. Multipass: pass through list a constant number of times to calculate something (length)


class ListNode:
    """
    Creates a singly linked list node.
    """
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = None

    def __str__(self):
        """
        Returns: contents of ListNode class in human readable form.
        """
        out = 'SLL ['
        if self != None:
            cur = self.next
            out = out + str(self.val)
            while cur != None:
                out = out + ' -> ' + str(cur.val)
                cur = cur.next
        out = out + ']'
        return out

class Solution:
    """
    Creates methods for testing ListNodes without using LinkedList class.
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        Find the node reference at which the intersection of two singly LL begins.
        Args:
            headA (ListNode): first node in list A
            headB (ListNode): first node in list B
        Returns:
            ListNode: intersection node or None
        """
        # Checks for an empty list.
        if not headA or not headB:
            return None

        # Sets pointers for LL iteration.
        pA, pB = headA, headB

        # Once list iteration completes, pointer switches to head of opposite 
        # list and vice versa. This accounts for cases of differing list lengths.
        while pA != pB:
            pA = headB if pA == None else pA.next
            pB = headA if pB  == None else pB.next

        return pA

    def copyRandomList(self, head: ListNode) -> ListNode:
        """
        A linked list is given such that each node contains an additional random pointer
        which could point to any node in the list or null. Return a deep copy of the list.
        Each node contains a random pointer that points to the index position of another node.
        Time complexity O(n), space complexity O(1).
        Args:
            head (ListNode): first node in the LL
        Returns:
            ListNode: deep copy of the LL
        """
        dic, prev, node = {}, None, head
        
        # Iterates through the original list.
        while node:
            
            # Uses a dictionary to map original node to its clone.
            if node not in dic:
                dic[node] = ListNode(node.val, node.next, node.val)
            
            # Previous node points to the clone.
            if prev:
                prev.next = dic[node]

            # If there is no prev, we are at the head node. Store it for later.
            else: 
                head = dic[node]

            if node.random:

                # If node.random points to a node that we have not yet encountered, store it in the dictionary.
                if node.random not in dic:
                    dic[node.random] = ListNode(node.random.val, node.random.next, node.random.random)

                # Make the copy's random property point to the copy instead of the original.
                dic[node].random = dic[node.random]

            # Store prev and advance to the next node.
            prev, node = dic[node], node.next

        return head

    def oddEvenList(self, head: ListNode) -> ListNode:
        """
        Given a SLL, group all even indexed nodes together followed by odd indexed nodes.
        Update the nodes in-place using O(1) space and O(n) time complexity.
        Args:
            head (ListNode): first node in the singly linked list
        Returns:
            ListNode: first node in the updated singly linked list
        """
        # Initializes head nodes and pointers for even and odd linked lists.
        evens = evenHead = ListNode(0)
        odds = oddHead = ListNode(0)
        count = 0
        
        # Iterates through the linked list.
        while head:
            
            # If the index is even, adds node to the evens LL.
            if count % 2 == 0:
                evens.next = head
                evens = evens.next
                
            # If the index is odd, adds node to the odds LL.
            else:
                odds.next = head
                odds = odds.next

            count += 1
            head = head.next
        
        # Attaches the odds LL to the end of the evens LL.
        evens.next = oddHead.next
        odds.next = None
            
        return evenHead.next

    def hasCycle(self, head):
        """
        Determines if a linked list contains a cycle utilizing 
        the Tortoise and the Hare algorithm.
        Args:
            head (object): the first node in the list
        Returns:
            bool: True if a cycle is present, else False
        """
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while fast and fast.next:
            if fast == slow or fast.next == slow:
                return True
            
            fast = fast.next.next
            slow = slow.next
        return False

        # Second method using try/except to catch non-cycles
        # try:
        #     slow = head
        #     fast = head.next
        #     while slow is not fast:
        #         slow = slow.next
        #         fast = fast.next.next
        #     return True
        
        # # Handles the case with no cycle using an exception.
        # except:
        #     return False

    def swapPairs(self, head: ListNode) -> ListNode:
        """
        Given a linked list, swap every two adjacent nodes and return its head node.
        Example: 1-> 2-> 3-> 4 should return 2-> 1-> 4-> 3.
        Args:
            head (ListNode): first item in the LL
        Returns:
            ListNode: first item in the LL
        """
        # Initializes variables to assist with iteration.
        prev, prev.next = self, head

        # Updates pointers in order to swap adjacent nodes.
        while prev.next and prev.next.next:
            node = prev.next
            after = node.next
            prev.next, after.next, node.next = after, node, after.next
            prev = node
        return self.next

    
class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with a front sentinel.
        """
        self.head = ListNode(None)

        # Populates SLL with initial values (if provided).
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form.
        """
        out = 'SLL ['
        if self.head.next != None:
            cur = self.head.next.next
            out = out + str(self.head.next.val)
            while cur != None:
                out = out + ' -> ' + str(cur.val)
                cur = cur.next
        out = out + ']'
        return out

    def add_front(self, value: object) -> None:
        """
        Adds a node behind the head node at the front of the LL.
        Args:
            value (object): value being added to the LL
        """
        new = ListNode(value)
        new.next = self.head.next
        self.head.next = new

    def add_back(self, value: object) -> None:
        """
        Adds a new node to the end of the list.
        Args:
            value (object): item being added to the LL
        """
        curr = self.head
        new = ListNode(value)

        # Iterates up to the last node.
        while curr.next != None:
            curr = curr.next
        
        # Adds new node behind the last node.
        new.next = curr.next
        curr.next = new

    def deleteNode(self, node):
        """
        Deletes a node (except the tail) in a singly linked list, 
        given only access to that node.
        Args:
            node (object): node to be deleted
        """
        # Due to no head node, we cannot iterate the LL.  Therefore,
        # we can only swap node values directly in order to remove a node.
        if node.next is not None:
            node.val, node.next = node.next.val, node.next.next

    def reverseList(self, head: ListNode) -> ListNode:
        """
        Utilizes iteration to reverse a singly linked list.
        Args:
            head (ListNode): head node of the SLL
        Returns:
            ListNode: new head node of the reversed SLL
        """
        # Initializes two nodes for traversing the SLL.
        prev, curr = None, head
        
        # Iterates through the list, updating pointers.
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        self.head.next = prev
        
        return prev

    def reverseRecur(self, head: ListNode, prev=None) -> ListNode:
        """
        Utilizes recursion to reverse a singly linked list.
        Args:
            head (ListNode): head.next node of the SLL
        Returns:
            ListNode: new head.next node of the reversed SLL
        """
        # Reached end of list, updates sentinel pointer.
        if not head:
            self.head.next = prev
            return prev
        
        # Updates pointers during recursive LL traversal.
        temp = head.next
        head.next = prev

        return self.reverseRecur(temp, head)

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        You are given two non-empty linked lists representing two non-negative integers. 
        The digits are stored in reverse order and each of their nodes contain a single 
        digit. Add the two numbers and return it as a linked list.
        Args:
            l1 (ListNode): first node in the list
            l2 (ListNode): first node in the second list
        Returns:
            ListNode: Linked list object
        """
        # Initializes the carry variable.
        carry = 0

        # Continues summation until there is no carry or further values.
        while l1 or l2 or carry:
            
            # Adds the two integer values and traverses to the next node.
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            # Special case if there is a carry.
            if carry >= 10:
                self.add_front(carry%10)
                carry = 1

            else: 
                self.add_front(carry)
                carry = 0
        return lst3

    def length(self) -> int:
        """
        Returns:
            int: the number of nodes in the SLL
        """
        count = 0
        curr = self.head.next

        # Iterates up to the last node.
        while curr:
            count +=1
            curr = curr.next

        return count

    def lengthRecur(self, curr=False) -> int:
        """
        Returns:
            int: the number of nodes in the SLL
        """
        if curr is False:
            curr = self.head.next
        if curr is None:
            return 0
        return 1 + self.lengthRecur(curr.next)

        


if __name__ == "__main__":

    
    list = LinkedList()
    list.add_front('C')
    list.add_front('B')
    list.add_front('A')
    print('\n# add_front example 1')
    print(list)

    
    # print('\n# length iteration')
    # print(list.length())
    # print('\n# length recursion')
    # print(list.lengthRecur())

    # list.reverseList(list.head.next)
    # print('\n# reverse example 1')
    # print(list)

    # list.reverseRecur(list.head.next)
    # print('\n# reverse example 2')
    # print(list)

    # curr = list.head
    # for _ in range(list.length()-1):
    #     curr = curr.next
    #     if curr.val == 'B':
    #         list.deleteNode(curr)
    # print('\n# remove node example')
    # print(list)

    # lst1 = LinkedList([6, 5, 3, 1])
    # lst2 = LinkedList([6, 4, 2])
    # lst3 = LinkedList()
    # lst3.addTwoNumbers(lst1.head.next, lst2.head.next)
    # print(lst3)


    # # Creates a linked list using just the ListNode class.
    # lst = ListNode()
    # node1 = ListNode(1)
    # node2 = ListNode(2)
    # node3 = ListNode(3)
    # node4 = ListNode(4)
    # node5 = ListNode(5)
    # lst.next = node1
    # node1.next = node2
    # node2.next = node3
    # node3.next = node4
    # node4.next = node5
    # print(node1)

    # # Tests the swapPairs method.
    # sol = Solution()
    # print(sol.swapPairs(lst.next))
   

    # # Tests the hasCycle method.
    # lst = ListNode(0)
    # node1 = ListNode(3)
    # node2 = ListNode(2)
    # node3 = ListNode(0)
    # node4 = ListNode(-4)
    # lst.next = node1
    # node1.next = node2
    # node2.next = node3
    # node3.next = node4
    # node4.next = node2
    # sol = Solution()
    # print(sol.hasCycle(lst.next))

    # # Tests the oddEvenList solution.
    # sol = Solution()
    # print(sol.oddEvenList(lst.next))

    # # Tests getIntersectionNode method.
    # node1 = ListNode(1)
    # node2 = ListNode(2)
    # node3 = ListNode(3)
    # node4 = ListNode(4)
    # node1.next = node2
    # node2.next = node3
    # node3.next = node4
    
    # lst1 = ListNode(5)
    # lst2 = ListNode(6)
    # lst3 = ListNode(7)
    # lst4 = node3
    # lst5 = node4
    # lst1.next = lst2
    # lst2.next = lst3
    # lst3.next = lst4
    # print(node1)
    # print(lst1)

    # sol = Solution()
    # print(sol.getIntersectionNode(node1, lst1))
                