def input_matrix(r, c):
    matrix = []
    for _ in range(r):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def output_matrix(matrix):
    for row in matrix:
        print(*row)

def horizontal_mirror(matrix):
    matrix.reverse()

def main():
    n, m = map(int, input().split())

    matrix = input_matrix(n, m)

    horizontal_mirror(matrix)

    output_matrix(matrix)

if __name__ == "__main__":
    main()