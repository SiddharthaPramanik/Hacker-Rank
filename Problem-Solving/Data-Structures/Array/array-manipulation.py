# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * (n + 1)
    for start, end , change in queries:
        arr[start - 1] += change
        if end < len(arr):
            arr[end] -= change
    
    arr_sum = 0
    arr_max = 0
    for num in arr[:-1]:
        arr_sum += num
        arr_max = max(arr_max, arr_sum)
    return arr_max

if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(str(result) + '\n')
