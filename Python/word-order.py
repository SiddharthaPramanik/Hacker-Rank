if __name__ == '__main__':
    n = int(input())
    count = {}
    
    for _ in range(n):
        s = input()
        if s in count:
            count[s] += 1
        else:
            count[s] = 1
    print(len(count))
    for key, value in count.items():
        print(value, end=" ")