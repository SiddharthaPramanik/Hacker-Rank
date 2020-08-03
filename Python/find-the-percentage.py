if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_score = student_marks[query_name]
    result = sum(query_score) / len(query_score)
    print("{:.2f}".format(result))