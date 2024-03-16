from itertools import product

def count_ways_to_paint(H, W, K, paper):
    def count_black_cells(paper):
        return sum(row.count('#') for row in paper)

    total_black_cells = count_black_cells(paper)
    result = 0

    for rows_to_paint in product([0, 1], repeat=H):
        for cols_to_paint in product([0, 1], repeat=W):
            current_black_cells = 0

            for i in range(H):
                for j in range(W):
                    if rows_to_paint[i] or cols_to_paint[j]:
                        current_black_cells += (paper[i][j] == '#')

            if current_black_cells == total_black_cells - K:
                result += 1

    return result

# Đọc input
H, W, K = map(int, input().split())
paper = [input().strip() for _ in range(H)]

# Tính và in ra kết quả
result = count_ways_to_paint(H, W, K, paper)
print(result)