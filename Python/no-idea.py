
def cal_happiness(arr, A, B):
    all_elements = A | B
    arr = [num for num in arr if num in all_elements ]
    return sum([(num in A) - (num in B) for num in arr])

if __name__ == "__main__":
    nm = input()
    n = int(nm.split()[0])
    m = int(nm.split()[1])

    arr = list( map( int, input().split() ) )
    A = set( map( int, input().split() ) )
    B = set( map( int, input().split() ) )

    result = cal_happiness(arr, A, B)
    print(result)
