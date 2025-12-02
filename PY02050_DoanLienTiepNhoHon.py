if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        res = [0] * n      # lưu kết quả cho từng vị trí
        st = []            # stack lưu chỉ số các phần tử

        for i in range(n):
            # Bỏ hết những vị trí bên trái có giá trị <= A[i]
            # vì chúng KHÔNG thể là "rào chắn" > A[i] nữa
            while st and a[st[-1]] <= a[i]:
                st.pop()

            # Nếu stack rỗng: không có phần tử nào bên trái > A[i]
            if not st:
                res[i] = i + 1
            else:
                # Gần nhất bên trái có A[k] > A[i]
                res[i] = i - st[-1]

            # Đưa vị trí hiện tại vào stack
            st.append(i)

        # In kết quả
        print(*res)
