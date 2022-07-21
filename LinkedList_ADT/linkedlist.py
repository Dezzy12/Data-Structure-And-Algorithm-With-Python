# Implementation of the LinkedList ADT
class LinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    # Produces a string representation of our linked list
    def __str__(self):
        if self._head is None:
            return "[]"
        else:
            ll_str = "["
            curr = self._head
            while curr is not None:
                ll_str = ll_str + str(curr.data) + " -> "
                curr = curr.next
            ll_str = ll_str + "None]"
            return ll_str

    # Returns the number of items in the linked list
    def __len__(self):
        length = 0
        curNode = self._head
        while curNode is not None:
            length += 1
            curNode = curNode.next
        return length

    # Determines if and item is in our linked list
    def __contains__(self, target):
        curNode = self._head
        while curNode is not None and curNode.data != target:
            curNode = curNode.next
        return curNode is not None

    # inserts a new item in our linked list
    def insert(self, data):
        newNode = ListNode(data)
        newNode.next = self._head
        self._head = newNode

    # Remove an instance of the dat from the linked list
    def remove(self, data):
        predNode = None
        curNode = self._head
        while curNode is not None and curNode.data != data:
            predNode = curNode
            curNode = curNode.next

        # item has to be in the list to remove it
        if curNode is not None:
            if curNode is self._head:
                self._head = curNode.next
            else:
                predNode.next = curNode.next
        else:
            print(" The data must be in the list before it can be removed ")

    # Searching for a Node
    def unsortedSearch(self, target):
        curNode = self._head
        while curNode is not None and curNode.data != target:
            curNode = curNode.next
        return curNode is not None

    # reverse our linked list
    def reversal(self):
        curNode = self._head
        prevNode = None
        while curNode is not None:
            revNode = prevNode
            prevNode = curNode
            curNode = curNode.next
            prevNode.next = revNode


# Defines a private storage class for creating list nodes
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
