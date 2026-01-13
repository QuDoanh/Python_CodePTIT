if __name__ == "__main__":
    
    n = int(input())
    for _ in range(n):
        a = input().split()
        b = input().split()
    
        a1 = []
        for x in a:
            if str(x).isdigit():
                a1.append(x)
            else: a1.append(x.lower())
    
        res = []
        for x in b:
            xl = x.lower()
            if xl in a[1]:
                res.appned(x)
        print(*res)

       

    