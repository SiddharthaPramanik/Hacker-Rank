
# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    freq = []
    for query in queries:
        matching = [s for s in strings if s == query]
        freq.append(len(matching))
    
    return freq

if __name__ == '__main__':

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    print('\n'.join(map(str, res)))