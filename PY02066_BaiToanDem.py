import sys

if __name__ == "__main__":
    data = sys.stdin.read().split()
    n = int(data[0])
    a= list(map(int, data[1:n+1]))


    check = False
    for i in range(1, a[-1] +1):
        if i not in a:
            print(i)
            check  = True
    
    if not check:
        print("Excellent!")