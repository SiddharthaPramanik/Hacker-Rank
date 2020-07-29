if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    winner = max(arr)
    arr.remove(winner)
    while max(arr) == winner:
        arr.remove(max(arr))
    print(max(arr))