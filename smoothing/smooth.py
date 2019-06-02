import numpy as np
from random import randint as rnd
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
        self.population = [{'pos': [rnd(4, self.w-5), rnd(4, self.h-5)], 'fit': 0} for _ in range(self.pop_size)]

    def density(self):
        values = np.array([self.binary[index] for index in self.kernel])
        white_amount = values[values == 255].size
        return round(white_amount/9, 2)

    def fitness(self):
        fitted = 0
        for p in self.population:
            if self.threshold[0] <= p['fit'] <= self.threshold[1]:
                fitted += 1
        return round(fitted/len(self.population), 2)

    def migrate(self):  # сделать так, чтобы мигрировала только часть - использовать формулы
        for point in self.population:
            delta_x = [-1, 1][rnd(0, 1)]
            delta_y = [-1, 1][rnd(0, 1)]
            if 1 < point['pos'][0] + delta_x < self.w - 5:
                point['pos'][0] += delta_x
            if 1 < point['pos'][1] + delta_y < self.h - 5:
                point['pos'][1] += delta_y

    def mutate_1(self, p):
        if p['fit'] > self.threshold[1]:
            self.binary[p['pos'][0], p['pos'][1]] = 0
        elif p['fit'] < self.threshold[0]:
            self.binary[p['pos'][0], p['pos'][1]] = 255

    def mutate_n(self, n: int):
        pass

    def get_kernel(self):
        i_range = range(-(self.kernel_size//2), self.kernel_size//2 + 1)
        j_range = list(range(-(self.kernel_size**2//2), (self.kernel_size**2)//2 + 1))
        for num, i in enumerate(i_range):
            for j in j_range[:self.kernel_size:self.kernel_size]:
                pass

    def start(self, steps):
        self.generate_population()
        for step in range(steps):
            for p in self.population:
                x = p['pos'][0]
                y = p['pos'][1]
                self.kernel = [(x - 1, y - 4), (x - 1, y - 3), (x - 1, y - 2),
                           (x, y - 1), (x, y), (x, y + 1),
                           (x + 1, y + 2), (x + 1, y + 3), (x + 1, y + 4)]
                p['fit'] = self.density()
                self.mutate_1(p)
            fit = self.fitness()
            print('step:', step, 'fitness:', fit)
            # if fit >= self.fit:
            #     return
            del self.population
            self.generate_population()
            # self.migrate()

    def get_image(self):
        return Image.fromarray(self.binary)

    def get_binary(self):
        return self.binary
