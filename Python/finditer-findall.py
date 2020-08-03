import re

if __name__ == '__main__':
    input_str = input()
    query_string = r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})([qwrtypsdfghjklzxcvbnm])'
    
    if re.search(query_string, input_str) is None:
        print(-1)
    else:
        for match in re.finditer(query_string, input_str, re.I):
            print(input_str[match.start() : match.end() - 1])
