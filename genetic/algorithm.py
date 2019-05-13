from random import randint as rnd
from PIL import Image, ImageDraw
from scipy.spatial import Delaunay
from genetic.coloring import color
from genetic.fitness import fitness


class Algorithm:

    def __init__(self, input_path, output_path='', points_amount=1000, steps=500):
        self.image_in = Image.open(input_path)  # input image
        self.image_out = Image.open(input_path)  # image that will be processed
        self.pixels = self.image_in.load()
        self.width, self.height = self.image_in.size
        self.layer = Image.new('RGBA', (self.width, self.height))
        self.draw = ImageDraw.Draw(self.layer)
        self.points_amount = points_amount
        self.points = []
        self.steps = steps

    def start(self):
        self.generate_points()
        for i in range(self.steps):
            self.draw_triangles()
            print(fitness(self.image_in.getdata(), self.image_out.getdata()))
            # self.mutate()

    def generate_points(self):
        self.points = [[0, 0], [0, self.height], [self.width, 0], [self.width, self.height]] +\
               [[rnd(0, self.width), rnd(0, self.height)] for _ in range(self.points_amount)]

    def mutate(self):
        for point in self.points:
            delta_x = rnd(-2, 2)
            delta_y = rnd(-2, 2)
            if point[0] + delta_x > self.width - 1:
                point[0] -= delta_x
            else:
                point[1] += delta_x
            if point[1] + delta_y > self.height - 1:
                point[1] -= delta_y
            else:
                point[1] += delta_y

    def draw_triangles(self):
        tri = Delaunay(self.points)
        for i in tri.simplices:
            a = tuple(self.points[i[0]])
            b = tuple(self.points[i[1]])
            c = tuple(self.points[i[2]])
            fill = color([a, b, c], self.pixels)
            self.draw.polygon([a, b, c], fill=fill)
        self.image_out.paste(self.layer, mask=self.layer)
