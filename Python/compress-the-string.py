import itertools

def repeat(char):
    return char
def compress(input_str):
    groups = itertools.groupby([char for char in input_str], repeat)
    result = []
    for key, group in groups:
        print(f"({len([count for count in group])}, {key})", end=" ")

if __name__ == '__main__':
    input_str = input()
    compress(input_str)