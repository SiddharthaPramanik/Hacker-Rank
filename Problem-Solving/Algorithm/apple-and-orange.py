
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_distance = [apple + a for apple in apples]
    orange_distance = [orange + b for orange in oranges]

    apple_count = 0
    orange_count = 0

    for distance in apples_distance:
        if (distance >= s) and (distance <= t):
            apple_count += 1

    for distance in orange_distance:
        if (distance >= s) and (distance <= t):
            orange_count += 1
    print(f"{apple_count}\n{orange_count}")

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
