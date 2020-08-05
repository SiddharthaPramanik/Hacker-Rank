#!/bin/python3

def equalizeArray(arr):
    
    count = {}

    for n in arr:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
    remove_elements = list(filter(lambda n : n != max(count, key=count.get), arr))
    return len(remove_elements)

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    print(result)