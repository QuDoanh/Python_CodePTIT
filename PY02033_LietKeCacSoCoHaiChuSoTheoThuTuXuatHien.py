
if __name__ == "__main__":
    s = input()
    res = []

    for i in range(0, len(s), 2):
        if(i+2 <= len(s)):
            tmp = int(s[i]+s[i+1])
            if(tmp not in res):
                res.append(tmp)
    
    for x in res:
        print(x, end = " ")
    print()