from math import cos, acos, pi, log, copysign, cosh, sinh


class Equations:
    @classmethod
    def linear(cls, a=1, b=0):
        return -b / a

    @classmethod
    def square(cls, a=1, b=0, c=0):
        d = b ** 2 - 4 * a * c
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return x1, x2

    @classmethod
    def cube(cls, g=1, a=0, b=0, c=0):
        if g == 0:
            return cls.square(a, b, c)
        if g == 0 and a == 0:
            return cls.linear(b, c)
        if g != 0 and c == 0:
            return 0, cls.square(g, a, b)
        # Делим на первый кооэфициент чтобы получить уравнение приведённого вида
        a /= g
        b /= g
        c /= g
        q = (a ** 2 - 3 * b) / 9
        r = (2 * a ** 3 - 9 * a * b + 27 * c) / 54
        s = q**3 - r**2
        if s > 0:
            t = acos(r / q ** 1.5) / 3
            x1 = -2 * q ** 0.5 * cos(t) - a / 3
            x2 = -2 * q ** 0.5 * cos(t + (2 * pi / 3)) - a / 3
            x3 = -2 * q ** 0.5 * cos(t - (2 * pi / 3)) - a / 3
        elif s < 0:
            t = (log(abs(r) / abs(q) ** 1.5 + ((abs(r) / abs(q) ** 1.5) ** 2 - 1) ** 0.5)) / 3
            x1 = -2 * copysign(1, r) * abs(q) ** 0.5 * cosh(t) - a / 3
            x2 = complex(copysign(1, r) * abs(q) ** 0.5 * cosh(t) - a / 3, (3 * abs(q)) ** 0.5 * sinh(t))
            x3 = complex(copysign(1, r) * abs(q) ** 0.5 * cosh(t) - a / 3, -(3 * abs(q)) ** 0.5 * sinh(t))
        else:
            x1 = -2 * r ** (1 / 3) - a / 3
            x2 = x3 = r ** (1 / 3) - a / 3
        return x1, x2, x3
