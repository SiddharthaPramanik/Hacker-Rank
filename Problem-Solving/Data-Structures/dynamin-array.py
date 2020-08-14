#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    N = []
    last_answer = 0

    for _ in range(n):
        N.append([])
    
    for query in queries:

        if query[0] == 1:
            x, y = query[1], query[2]
            N[((x ^ last_answer) % n)].append(y)
        else:
            x, y = query[1], query[2]
            last_answer = N[((x ^ last_answer) % n)][y % len(N[((x ^ last_answer) % n)])]
            print(last_answer)

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    dynamicArray(n, queries)
