import sys
import re

if __name__ == "__main__":
    n = int(input())
    d = {}
    for _ in range(n):
        for word in input().split():
            word = word.lower()
            id = 0
            for i in range(len(word)):
                if(not word[i].isdigit() and  not word[i].isalpha()):
                    word1 = word[id:i]
                    if(len(word1.strip()) >0):
                        if word1 not in d:
                            d[word1] =1
                        else: d[word1]+=1
                    id = i+1

            if id < len(word):
                tmp = word[id:]
                if(len(tmp.strip()) > 0):
                    if tmp in d:
                        d[tmp] +=1
                    else: d[tmp] =1
    
    res = list(d.items())
    res.sort(key = lambda x : (-x[1], x[0]))

    for x ,y in res:
        print(x, y)