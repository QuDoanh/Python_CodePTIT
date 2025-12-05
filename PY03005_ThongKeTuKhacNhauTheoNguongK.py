
if __name__ ==  "__main__":
    n,k  = list(map(int, input().split()))
    d = {}
    for _ in range(n):
        line = input().strip().split()

        for word in line:
            id = 0
            word = word.lower()

            for i in range(len(word)):
                if not word[i].isdigit() and not word[i].isalpha():
                    word1 = word[id:i]
                    if(len(word1.strip()) >0):
                        if word1 not in d:
                            d[word1] = 1
                        else: d[word1] += 1
                    id = i+1
            if id < len(word):
                word2 = word[id:]
                if word2 in d:
                    d[word2] += 1
                else: d[word2] =1 
    
    res = list(d.items())
    res.sort(key= lambda x : (-x[1], x[0]))

    for x, y in res:
        if(y >= k):
            print(x, y)
