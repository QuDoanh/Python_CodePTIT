import sys

def chuanHoa(x):
    tmp = x.split()
    if not tmp:
        return ""
    res = ""
    res += tmp[0][0].upper() + tmp[0][1:]
    for i in range(1, len(tmp)):
        res += " " + tmp[i]
    res = res.strip()
    if res[-1] not in ".!?":
        res += '.'
    return res


if __name__ == "__main__":
    data = sys.stdin.read().splitlines()

    sentences = []
    for line in data:
        line = line.lower().strip()
        if line == "": continue

        tmp = ""
        for ch in line:
            if ch in ".?!":
                tmp = tmp.strip() + ch
                sentences.append(chuanHoa(tmp))
                tmp = ""
            else:
                tmp += ch

        if tmp.strip() != "":
            sentences.append(chuanHoa(tmp))
        
    for x in sentences:
        print(x)
