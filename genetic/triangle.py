from math import fabs
# property


class Triangle:

    def __init__(self, a: int, b: int, c: int, points: list):
        self.points = points
        self.a = points[a]
        self.b = points[b]
        self.c = points[c]

        self.delta_a = [0, 0]
        self.delta_b = [0, 0]
        self.delta_c = [0, 0]

    def points_relation(self):
        x = (self.a[0], self.b[0], self.c[0])
        y = (self.a[1], self.b[1], self.c[1])
        xmin = min(x)
        ymin = min(y)
        xmax = max(x)
        ymax = max(y)

        rel = {}





    def area(self):
        det = (self.a[0] - self.c[0]) * (self.b[1] - self.c[1]) - (self.a[1] - self.c[1]) * (self.b[0] - self.c[0])
        return fabs(det) / 2

    def mutate(self, pixels):
        color_a = pixels[self.a[0], self.a[1]]
        color_b = pixels[self.b[0], self.b[1]]
        color_c = pixels[self.c[0], self.c[1]]



        if color_a == color_b == color_c:

            self.a[0] += 5
            self.a[1] += 5

            self.b[0] += 5
            self.b[1] += 5

            self.c[0] += 5
            self.c[1] += 5

            return 3

        if (color_a == color_b) or (color_a == color_c) or (color_c == color_b):
            if color_a == color_b:
                self.c[0] += 1
                self.c[1] += 1
            return 2

        self.a[0] -= 3
        self.a[1] -= 3

        self.b[0] -= 3
        self.b[1] -= 3

        self.c[0] -= 3
        self.c[1] -= 3

        return 1


