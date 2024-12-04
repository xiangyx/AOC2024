def count_string_occurrences(matrix, target):
    def search_from(x, y, dx, dy):
        n = len(matrix)
        m = len(matrix[0])
        for i in range(len(target)):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m or matrix[nx][ny] != target[i]:
                return False
        return True

    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]

    count = 0
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(m):
            for dx, dy in directions:
                if search_from(i, j, dx, dy):
                    count += 1

    return count

def count_x_pattern(matrix):
    n = len(matrix)
    m = len(matrix[0])
    count = 0

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if (
                (matrix[i-1][j-1] == 'M' and matrix[i-1][j+1] == 'M' and
                 matrix[i+1][j-1] == 'S' and matrix[i+1][j+1] == 'S' and matrix[i][j] == 'A')
                or
                (matrix[i-1][j-1] == 'S' and matrix[i-1][j+1] == 'M' and
                 matrix[i+1][j-1] == 'S' and matrix[i+1][j+1] == 'M' and matrix[i][j] == 'A')
                or
                (matrix[i-1][j-1] == 'S' and matrix[i-1][j+1] == 'S' and
                 matrix[i+1][j-1] == 'M' and matrix[i+1][j+1] == 'M' and matrix[i][j] == 'A')
                or
                (matrix[i-1][j-1] == 'M' and matrix[i-1][j+1] == 'S' and
                 matrix[i+1][j-1] == 'M' and matrix[i+1][j+1] == 'S' and matrix[i][j] == 'A')
            ):
                count += 1

    return count

def main():
    word_search = []
    with open("input/04.txt", "r") as f:
        for line in f:
            word_search.append(list(line.strip()))
    
    target = "XMAS"
    Q1_count = count_string_occurrences(word_search, target)
    Q2_count = count_x_pattern(word_search)
    print(f"answer to Q1: {Q1_count}")
    print(f"answer to Q2: {Q2_count}")

if __name__ == "__main__":
    main()