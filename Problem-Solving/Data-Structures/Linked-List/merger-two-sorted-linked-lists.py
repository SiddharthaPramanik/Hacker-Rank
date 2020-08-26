#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            print(sep)
 
# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def moveNode(source, target):
    # create a new node with the data from the source i.e existing linked list
    new_node = SinglyLinkedListNode(source.data)
    # point the next of new node to next of combined linked list.
    # this will be None as we are moving the tail and only pass the last node of tail
    new_node.next = target.next
    # connect the pointer/ next of last node of combined list to new node
    target.next = new_node

def mergeLists(head1, head2):
    
    # Check if both the lists are empty
    if (head1 is None) and (head2 is None):
        return None

    # Create a dummy node for combined linked list
    head = SinglyLinkedListNode(0)
    # Creating a copy of head to move forward and add at tail
    tail = head

    while True:
        # check for empty head1
        if head1 is None:
            tail.next = head2
            return head.next
        else:
            # check for empty head2
            if head2 is None:
                tail.next = head1
                return head.next
            else:
                # If head1 data is smaller add the node to new linked list
                if head1.data < head2. data:
                    # moveNode will add the node to the new linked list
                    moveNode(head1, tail)
                    # move to next node in head1
                    head1 = head1.next
                    # move to last node in new linked list
                    tail = tail.next
                else:
                    # moveNode will add the node to the new linked list
                    moveNode(head2, tail)
                    # move to next node in head2
                    head2 = head2.next
                    # move to last node in new liked list
                    tail = tail.next
    # return the head of new linked list except for the head as that is a dummy node
    return head.next

    

if __name__ == '__main__':

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ')
