from random import randint as rnd
from PIL import Image, ImageDraw
from scipy.spatial import Delaunay
from genetic.coloring import color
from genetic.fitness import fitness


class Algorithm:

    def __init__(self, input_path, points_amount=1000, steps=1):
        self.image_in = Image.open(input_path)  # input image
        self.image_out = Image.open(input_path)  # image that will be processed
        self.pixels = self.image_in.load()
        self.width, self.height = self.image_in.size
        self.layer = Image.new('RGBA', (self.width, self.height))
        self.draw = ImageDraw.Draw(self.layer)
        self.points_amount = points_amount
        self.points = []
        self.steps = steps
        self.fit_val = None

    def start(self, iters=None):
        fit_vals = {}
        if iters:
            self.steps = iters
        self.generate_points()
        best_image = []
        best = 20_000_000_000
        for i in range(self.steps):
            self.draw_triangles()
            fit = fitness(self.image_in.getdata(), self.image_out.getdata())
            if best > fit:
                best = fit
                if best_image:
                    best_image.clear()
                best_image.append(self.image_out)
            print('last:', fit, 'best:', best)
            self.mutate()
            fit_vals[i] = best
        self.fit_val = best
        self.image_out = best_image[-1]
        return fit_vals

    def generate_points(self):
        self.points = [[0, 0], [0, self.height], [self.width, 0], [self.width, self.height]] +\
               [[rnd(0, self.width), rnd(0, self.height)] for _ in range(self.points_amount)]

    def mutate(self):
        for point in self.points:
            delta_x = [-1, 1][rnd(0, 1)]
            delta_y = [-1, 1][rnd(0, 1)]
            if 1 < point[0] + delta_x < self.width - 1:
                point[0] += delta_x
            if 1 < point[1] + delta_y < self.height - 1:
                point[1] += delta_y

    def draw_triangles(self):
        tri = Delaunay(self.points)
        for i in tri.simplices:
            poly = [tuple(self.points[i[j]]) for j in (0, 1, 2)]
            self.draw.polygon(poly, fill=color(poly, self.pixels))
        self.image_out.paste(self.layer, mask=self.layer)

    def show(self):
        self.image_out.show()
