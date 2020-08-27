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

# Complete the removeDuplicates function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def removeDuplicates(head):
    if head is None:
        return head
    else:
        temp = head
        while temp.next is not None:
            # check if the current node and the next node have same value
            if temp.data == temp.next.data:
                # change the next of current node so that it skips next node
                temp.next = temp.next.next
            else:
                # move the node to next node only if no chnage is needed
                # else you will miss the same value occuring thrice or more in a row
                temp = temp.next
    return head

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = removeDuplicates(llist.head)

        print_singly_linked_list(llist1, ' ')
        print('\n')
