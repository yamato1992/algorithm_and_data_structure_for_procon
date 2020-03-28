from typing import List
import math

def koch_curve(n: int, p1: List[float], p2: List[float]):
    if n == 0:
        return
    p1x, p1y = p1
    p2x, p2y = p2
    s = [(r - l) / 3 + l for (l, r) in zip(p1, p2)]
    t = [(r - l) * 2 / 3 + l for (l, r) in zip(p1, p2)]
    sx, sy = s
    tx, ty = t
    ux = (tx - sx) * math.cos(math.radians(60)) - (ty - sy) * math.sin(math.radians(60)) + sx
    uy = (tx - sx) * math.sin(math.radians(60)) + (ty - sy) * math.cos(math.radians(60)) + sy
    u = [ux, uy]
    n -= 1
    koch_curve(n, p1, s)
    print(*s)
    koch_curve(n, s, u)
    print(*u)
    koch_curve(n, u, t)
    print(*t)
    koch_curve(n, t, p2)

n = int(input())
p1 = [0, 0]
p2 = [100, 0]
print(*p1)
koch_curve(n, p1, p2)
print(*p2)