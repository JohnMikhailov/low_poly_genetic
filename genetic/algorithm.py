from random import randint as rnd
from PIL import Image, ImageDraw
import numpy as np
import matplotlib.path as mp
from collections import defaultdict
from scipy.spatial import Delaunay
from genetic.coloring import color
from genetic.fitness import fitness


class Algorithm:

    def __init__(self, input_path, output_path, points_amount, steps=500):
        self.image_in = Image.open(input_path)  # input image
        self.image_out = Image.open(input_path)  # image that will be processed
        self.pixels = self.image_in.load()
        self.width, self.height = self.image_in.size
        self.layer = Image.new('RGBA', (self.width, self.height))
        self.draw = ImageDraw.Draw(self.layer)
        self.points_amount = points_amount
        self.steps = steps

    def start(self):
        points = self.generate_points()
        for i in range(self.steps):
            self.draw_triangles(points)
            print(fitness(self.image_in, self.image_out))
            self.mutate()

    def generate_points(self):
        return [[0, 0], [0, self.height], [self.width, 0], [self.width, self.height]] +\
               [[rnd(0, self.width), rnd(0, self.height)] for _ in range(self.points_amount)]

    def mutate(self):
        pass

    def draw_triangles(self, points):
        tri = Delaunay(points)
        for i in tri.simplices:
            a = tuple(points[i[0]])
            b = tuple(points[i[1]])
            c = tuple(points[i[2]])
            fill = color([a, b, c], self.pixels)
            self.draw.polygon([a, b, c], fill=fill)
        self.image_out.paste(self.layer, mask=self.layer)
