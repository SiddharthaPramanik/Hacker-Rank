if __name__ == '__main__':
    nested_list = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        nested_list.append([name, score])
    
    min_score = min(scores)
    second_min_score = max(scores)
    for item in nested_list:
        if item[1] < second_min_score and item[1] > min_score:
            second_min_score = item[1]
    second_min_names = [item[0] for item in nested_list if item[1] == second_min_score]
    second_min_names.sort()
    for name in second_min_names:
        print(name)