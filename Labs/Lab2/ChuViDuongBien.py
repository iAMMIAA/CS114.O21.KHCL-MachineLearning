def tinh_chu_vi_duong_bien(m, n, matran):
    chu_vi = 0

    for i in range(m):
        for j in range(n):
            if matran[i][j] == 1:
                if i == 0 or matran[i - 1][j] == 0: 
                    chu_vi += 1
                if i == m - 1 or matran[i + 1][j] == 0:  
                    chu_vi += 1
                if j == 0 or matran[i][j - 1] == 0:  
                    chu_vi += 1
                if j == n - 1 or matran[i][j + 1] == 0: 
                    chu_vi += 1

    return chu_vi

m, n = map(int, input().split())
matran = []
for _ in range(m):
    row = list(map(int, input().split()))
    matran.append(row)

ket_qua = tinh_chu_vi_duong_bien(m, n, matran)

print(ket_qua)