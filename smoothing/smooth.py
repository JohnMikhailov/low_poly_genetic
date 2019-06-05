import numpy as np
from random import randint as rnd, choice
import itertools


class Smooth:

    def __init__(self, binary, size, threshold=(0.2, 0.5), fit=0.5, radius=2):
        self.binary = binary
        self.w, self.h = self.binary.shape
        self.size = size
        self.threshold = threshold
        self.fit = fit
        self.kernel_size = radius
        self.population = None
        self.kernel = None

    def generate_population(self):
        self.population = [{'pos': [rnd(0, self.w),
                                    rnd(0, self.h)], 'density': 0}
                           for _ in range(self.size)]

    def kernel_density(self):
        values = np.array([self.binary[index] for index in self.kernel if index[0] < self.w and index[1] < self.h])
        white_amount = values[values == 255].size
        return round(white_amount/len(self.kernel), 2)

    def fitness(self):
        fitted = 0
        for p in self.population:
            x, y = p['pos']
            self.set_kernel(x, y)
            if self.threshold[0] < self.kernel_density() < self.threshold[1]:
                fitted += 1
        return round(fitted/len(self.population), 2)

    def migrate(self):
        for point in self.population:
            if not (self.threshold[0] < point['density'] < self.threshold[1]):
                point['pos'] = [rnd(0, self.w), rnd(0, self.h)]

    def mutate(self, p):
        if p['density'] > self.threshold[1]:
            for i, j in self.kernel:
                self.binary[i, j] = 0
        if p['density'] < self.threshold[0]:
            for i, j in [choice(self.kernel)]:
                self.binary[i, j] = 255

    def set_kernel(self, x, y):
        radius = self.kernel_size
        _x, _y = [x], [y]
        for i in range(1, radius + 1):
            _x += [x - i, x + i]
            _y += [y - i, y + i]
        ker = itertools.product(_x, _y)
        self.kernel = [(i, j) for i, j in ker if i < self.w and j < self.h]

    def start(self, steps=1):
        self.generate_population()
        if self.fitness() >= self.fit:
            return
        for step in range(steps):
            for p in self.population:
                x = p['pos'][0]
                y = p['pos'][1]
                self.set_kernel(x, y)
                p['density'] = self.kernel_density()
                self.mutate(p)
            fit = self.fitness()
            print('step:', step, 'fitness:', fit)
            if fit >= self.fit:
                return
            self.migrate()

    def get_binary(self):
        return self.binary
