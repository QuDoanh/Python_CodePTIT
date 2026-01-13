
if __name__ == "__main__":
    s = set()
    with open("CONTACT.in", "r") as f:
        for line in f:
            email = line.strip()
            if not email:
                continue
            email = email.lower()
            s.add(email)
    res = sorted(s)
    for x in res:
        print(x)