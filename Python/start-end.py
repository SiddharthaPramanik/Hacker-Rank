import re

input_str = input()
query_str = input()

if re.search(query_str, input_str):
    index = 0
    while (index + len(query_str) < len(input_str)):
        match = re.search(query_str, input_str[index:])
        if match is not None:
            print(f"({index + match.start()}, {index + match.end() - 1})")
            index += match.start() + 1
        else:
            break
else:
    print("(-1, -1)")