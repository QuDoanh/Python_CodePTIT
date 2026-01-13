if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        s = input()
        tongChan = 0
        tichLe = 1
        for i in range(len(s)):
            digit = int(s[i])
            if (i + 1) % 2 == 0:      
                tongChan += digit
            else:
                if digit != 0:        
                    tichLe *= digit
        
        if tongChan == 0:
            print("INVALID")
        else:
            res = tichLe/ tongChan 
            print(f"{res:.6f}")
