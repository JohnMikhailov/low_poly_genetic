import numpy as np
from random import randint as rnd, sample, choice
from PIL import Image


class Smooth:

    def __init__(self, binary, pop_size, threshold=(0.2, 0.5), fit=0.5, kernel_size=3):
        self.binary = binary
        self.w, self.h = self.binary.shape
        self.pop_size = pop_size
        self.threshold = threshold
        self.fit = fit
        self.kernel_size = kernel_size
        self.population = None
        self.kernel = None

    def generate_population(self):
        self.population = [{'pos': [rnd(0, self.w),
                                    rnd(0, self.h)], 'density': 0}
                           for _ in range(self.pop_size)]

    def density(self):
        values = np.array([self.binary[index] for index in self.kernel if index[0] < self.w and index[1] < self.h])
        white_amount = values[values == 255].size
        return round(white_amount/9, 2)

    def fitness(self):
        fitted = 0
        for p in self.population:
            x, y = p['pos']
            self.kernel = self.get_kernel(x, y)
            if self.threshold[0] < self.density() < self.threshold[1]:
                fitted += 1
        return round(fitted/len(self.population), 2)

    def migrate(self):
        for point in self.population:
            if not (self.threshold[0] < point['density'] < self.threshold[1]):
                point['pos'].clear()
                point['pos'] += [rnd(0, self.w), rnd(0, self.h)]

    def mutate_all(self, p):
        if p['density'] > self.threshold[1]:
            for i, j in self.kernel:
                self.binary[i, j] = 0
        if p['density'] < self.threshold[0]:
            for i, j in [choice(self.kernel + [(0, 0)])]:
                self.binary[i, j] = 255

    def get_kernel(self, x, y):
        i_range = range(-(self.kernel_size//2), self.kernel_size//2 + 1)
        j_range = list(range(-(self.kernel_size**2//2), (self.kernel_size**2)//2 + 1))
        deltas = []
        for num, i in enumerate(i_range):
            for j in j_range[num * self.kernel_size:(num + 1) * self.kernel_size]:
                deltas.append((i, j))
        return [(x + i, y + j) for i, j in deltas if x + i < self.w and y + j < self.h]

    def start(self, steps=1):
        self.generate_population()
        if self.fitness() >= self.fit:
            return
        for step in range(steps):
            for p in self.population:
                x = p['pos'][0]
                y = p['pos'][1]
                self.kernel = self.get_kernel(x, y)
                p['density'] = self.density()
                self.mutate_all(p)
            fit = self.fitness()
            print('step:', step, 'fitness:', fit)
            if fit >= self.fit:
                return
            self.migrate()

    def get_binary(self):
        # for i, j in [(0, 0), (0, self.h - 1), (self.w - 1, 0), (self.w - 1, self.h - 1)]:
        #     self.binary[i, j] = 255
        return self.binary
