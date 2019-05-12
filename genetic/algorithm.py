from scipy.spatial import Delaunay
from genetic.fitness import fitness
from random import randint as rnd
from PIL import Image, ImageDraw


class Algorithm:

    def __init__(self, input_path, output_path, points_amount):
        self.image = Image.open(input_path)
        self.width, self.height = self.image.size
        self.draw = ImageDraw.Draw(Image.new('RGBA', (self.width, self.height)))
        self.points_amount = points_amount

    def generate_points(self):
        return [(0, 0), (0, self.height), (self.width, 0), (self.width, self.height)] +\
               [(rnd(0, self.width), rnd(0, self.height)) for _ in range(self.points_amount)]




