#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            print(sep)

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):

    new_node = DoublyLinkedListNode(data)

    # Check if we have an empty list
    if head is None:
        head.data = data
        return head
    
    # Check if we have single element list
    if head.next is None:
        # create a copy of head
        temp_ptr = head
        
        # change the pointers for current and new node
        temp_ptr.next = new_node
        new_node.prev = temp_ptr
        new_node.next = None
        return head
    
    # If the data needs to be inserted at the begning of the list
    if head.data >= new_node.data:
        new_node.next = head
        new_node.next.prev = new_node
        head = new_node
        return head      

    current =  head

    # locate the loop after which we need to insert 
    while (current.next is not None) and (current.next.data < new_node.data):
        current = current.next
    
    # Make appropriate links
    new_node.next = current.next
    
    # If the node is not a the end of the list
    if current.next is not None:
        new_node.next.prev = new_node

    current.next = new_node
    new_node.prev = current

    return head

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ')
        print('\n')