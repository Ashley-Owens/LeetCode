# CodePath Advanced Interview Prep Course
# Linked List Practice Problems
# 8/18/2020


class ListNode:
    """
    Creates a singly linked list node.
    """
    def __init__(self, value):
        self.val = value
        self.next = None

class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with a front sentinel.
        """
        self.head = ListNode(None)

        # Populates SLL with initial values (if provided).
        if start_list is not None:
            for value in start_list:
                self.add_front(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
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
        prev, curr = None, self.head.next
        
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


if __name__ == "__main__":

    
    list = LinkedList()
    list.add_front('C')
    list.add_front('B')
    list.add_front('A')
    print('\n# add_front example 1')
    print(list)

    # list.reverseList(list.head)
    # print('\n# reverse example 1')
    # print(list)

    list.reverseRecur(list.head.next)
    print('\n# reverse example 2')
    print(list)

    # curr = list.head
    # for _ in range(list.length()-1):
    #     curr = curr.next
    #     if curr.val == 'B':
    #         list.deleteNode(curr)
    # print('\n# remove node example')
    # print(list)
    

                