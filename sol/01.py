def get_data():
    left = []
    right = []

    with open('input/01.txt', 'r') as f:
        for line in f:
            line = line.split()
            left.append(int(line[0]))
            right.append(int(line[1]))
    
    return left, right

def l1_norm(x, y):
    return sum([abs(x-y) for x, y in zip(x, y)])

def get_occurrences(lst):
    occurrences = {}
    for i in lst:
        if i in occurrences:
            occurrences[i] += 1
        else:
            occurrences[i] = 1
    return occurrences

def get_similarity_score(x, y):
    socre = 0
    y_occurrences = get_occurrences(y)
    for i in x:
        if i in y_occurrences:
            socre += i * y_occurrences[i]
    return socre

def main():
    left, right = get_data()
    total_distance = l1_norm(sorted(left), sorted(right))
    similarity_score = get_similarity_score(left, right)
    print(f"answer to Q1: {total_distance}")
    print(f"answer to Q2: {similarity_score}")

if __name__ == '__main__':
    main()