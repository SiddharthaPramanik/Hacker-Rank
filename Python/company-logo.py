
if __name__ == '__main__':
    s = input()
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    alpha_sort = sorted(count.items(), key=lambda x: x[0])
    for key, value in sorted(alpha_sort, key=lambda x: x[1], reverse=True)[:3]:
        print(key, value)

