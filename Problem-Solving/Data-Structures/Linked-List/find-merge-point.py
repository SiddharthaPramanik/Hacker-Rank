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

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def length(head):
    '''Function to fint the length of a linked list'''
    temp = head
    l = 0
    while temp is not None:
        l += 1
        temp = temp.next
    return l

def findMergeNode(head1, head2):
    '''Function to find the merge point of linked list'''
    # Find the lengths 
    head1_len = length(head1)
    head2_len = length(head2)
    
    # We are ssuming head1 is the longer list,
    # Swap the head nodes if head2 is longer
    if head2_len > head1_len:
        temp = head1
        head1 = head2
        head2 = temp

    # Find the length difference
    len_dif = abs(head1_len - head2_len)

    # Move head1 forward for "differnce in length" times
    for _ in range(len_dif):
        head1 = head1.next
    
    # Compare the list nodes from both lists untill a match is found
    while (head1 is not None) and (head2 is not None):
        if head1 == head2:
            return head1.data
        head1 = head1.next
        head2 = head2.next

    # First Solution
    # Compare all the nodes of one linked list to another
    # while head1:
    #     temp = head2
    #     while temp:
    #         if head1.next == temp.next:
    #             return head1.next.data
    #         temp = temp.next
    #     head1 = head1.next

if __name__ == '__main__':

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

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
            
        ptr1 = llist1.head
        ptr2 = llist2.head

        for i in range(llist1_count):
            if i < index:
                ptr1 = ptr1.next
                
        for i in range(llist2_count):
            if i != llist2_count-1:
                ptr2 = ptr2.next

        ptr2.next = ptr1

        result = findMergeNode(llist1.head, llist2.head)

        print(str(result) + '\n')
        # print('-'*10)
        # print_singly_linked_list(llist1.head, ' ')
        # print('-'*10)
        # print_singly_linked_list(llist2.head, ' ')