import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)
    
class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def peri(self):
        a = self.p1.dist(self.p2)
        b = self.p2.dist(self.p3)
        c = self.p1.dist(self.p3)
        if a + b > c and b + c > a and a + c > b:
            return f"{(a + b + c):.3f}"
        else:
            return "INVALID"

t = int(input())
arr = []
for _ in range(t):
    for x in input().split():
        arr.append(float(x))
i = 0
for _ in range(t):
    tri = Triangle(Point(arr[i], arr[i + 1]), Point(arr[i + 2], arr[i + 3]), Point(arr[i + 4], arr[i + 5]))
    i += 6
    print(tri.peri())