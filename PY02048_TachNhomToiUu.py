
if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    a = list(map(int , input().split()))

    a.sort()

    group = 1
    for i in range(0, n-1):
        if(a[i+1] - a[i] <= k):
            continue
        else:
            group +=1
    print(group)