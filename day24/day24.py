import sympy

class Hailstone:
    def __init__(self, sx, sy, sz, vx, vy, vz):
        self.sx = sx
        self.sy = sy
        self.sz = sz
        self.vx = vx
        self.vy = vy
        self.vz = vz

        self.a = vy
        self.b = -vx
        self.c = vy * sx - vx * sy

    def __repr__(self):
        return "Hailstone {" + f"a={self.a}, b={self.b}, c={self.c}" + "}"


def part1():
    hailstones = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        for line in lines:
            hailstones.append(Hailstone(*map(int, line.replace("@", ",").split(","))))

    res = 0
    for i, hs1 in enumerate(hailstones):
        for hs2 in hailstones[:i]:
            a1, b1, c1 = hs1.a, hs1.b, hs1.c
            a2, b2, c2 = hs2.a, hs2.b, hs2.c
            if a1 * b2 == a2 * b1:
                continue
            x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
            y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)
            if 200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000:
                if all((x - hs.sx) * hs.vx >= 0 and (y - hs.sy) * hs.vy >= 0 for hs in (hs1, hs2)):
                    res += 1

    return res

def part2():
    hailstones = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        for line in lines:
            hailstones.append(tuple(map(int, line.replace("@", ",").split(","))))

    xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr yr zr vxr vyr vzr")

    equations = []
    for sx, sy, sz, vx, vy, vz in hailstones:
        equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
        equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))


    sol = sympy.solve(equations)[0]
    return int(sol[xr] + sol[yr] + sol[zr])




if __name__ == "__main__":
    print(part1())
    print(part2())
