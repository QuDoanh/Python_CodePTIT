from datetime import datetime, date
import math
d1 = datetime.strptime(input(), "%d/%m/%Y")
d2 = datetime.strptime(input(), "%d/%m/%Y")

d1_chuan = datetime.strftime(d1, "%d/%m/%Y")
res = d2 - d1
print(d1_chuan)
print(d2)
print(res.days)


    # def lamTron(x):
    #     tmp = x - int(x)
    #     if tmp < 0.5:
    #         return int(x)
    #     return int(x) +1

def lamTronChuan(x):
    if x >= 0:
        return int(x + 0.5)
    return int(x-0.5)


def sang(n):
    prime = [True] * (n+1)

    prime[0]=  prime[1] = False

    for i in range(2, math.isqrt(n) + 1):
        if prime[i] ==True:
            for j in range(i*i, n+1, i):
                prime[j] = False
    return prime