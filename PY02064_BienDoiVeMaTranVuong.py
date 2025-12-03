if __name__ == "__main__":
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    # Trường hợp N > M: xóa hàng lẻ
    if N > M:
        need_remove = N - M
        rows_keep = []
        for i in range(1, N + 1):  
            if i % 2 == 1 and need_remove > 0:  
                need_remove -= 1
            else:
                rows_keep.append(i - 1) 

        B = [A[i] for i in rows_keep]

    # Trường hợp M > N: xóa cột chẵn
    elif M > N:
        need_remove = M - N
        cols_keep = []
        for j in range(1, M + 1): 
            if j % 2 == 0 and need_remove > 0: 
                need_remove -= 1
            else:
                cols_keep.append(j - 1)  

        B = []
        for i in range(N):
            B.append([A[i][j] for j in cols_keep])

    # Trường hợp đã vuông sẵn
    else:
        B = A

    for row in B:
        print(*row)