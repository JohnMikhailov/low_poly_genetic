import numpy as np
from random import randint as rnd


class Smooth:

    def __init__(self, binary, pop_size, threshold=0.5, kernel_size=3):
        self.binary = binary
        self.pop_size = pop_size
        self.threshold = threshold
        # self.kernel_size = kernel_size
        self.population = None

    def generate_population(self):
        w, h = self.binary.shape
        self.population = [{'pos': [rnd(1, w-1), rnd(1, h-1)], 'fit': 0} for _ in range(self.pop_size)]

    def __kernel_3x3(self, i, j):
        return [(i - 1, j - 4), (i - 1, j - 3), (i - 1, j - 2),
                (i, j - 1), (i, j), (i, j + 1),
                (i + 1, j + 2), (i + 1, j + 3), (i + 1, j + 4)]

    def start(self, steps):
        self.generate_population()
        for p in self.population:
            x = p['pos'][0]
            y = p['pos'][1]
            indices = self.__kernel_3x3(x, y)
            values = [self.binary[index] for index in indices]


