def merge_the_tools(string, k):
    result = []
    for i in range(len(string) // k):
        k_substring = []
        substring = string[:k]
        for c in substring:
            if c not in k_substring:
                k_substring.append(c)
        string = string[k:]
        result.append("".join(k_substring))
    print("\n".join(result))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)