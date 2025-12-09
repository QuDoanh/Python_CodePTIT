import sys

if __name__ == "__main__":
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    a = list(map(int, data[1:1+n]))

    dayChan = [ x for x in a if x %2  ==0]
    dayLe = [x for x in a if x % 2 == 1]

    dayChan.sort()
    dayLe.sort(reverse= True)
    id_chan = 0
    id_le = 0

    for i in range(n):
        if a[i] %2 == 0:
            a[i] = dayChan[id_chan]
            id_chan+=1
        else:
            a[i] = dayLe[id_le]
            id_le += 1
    
    for x in a:
        print(x, end =" ")
    