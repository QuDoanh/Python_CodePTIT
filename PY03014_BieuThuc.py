if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        s = input()

        ketQua = []
        stack = []
        cnt = 0
        for i in range(len(s)):
            if s[i] == '(':
                cnt += 1
                stack.append(cnt)
                ketQua.append(cnt)
            elif s[i] == ')':
                if stack:
                    dong = stack.pop()
                    ketQua.append(dong)
        
        for x in ketQua:
            print(x, end = " ")
        print()
