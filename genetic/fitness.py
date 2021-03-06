import math
import numpy as np


def fit(im1, im2):
    return np.sqrt(np.sum((im1 - im2)**2))


def fitness(original, selected):
    fit = 0
    for i in range(len(original)):
        r = original[i][0] - selected[i][0]
        g = original[i][1] - selected[i][1]
        b = original[i][2] - selected[i][2]
        fit += r*r + g*g + b*b
    return math.sqrt(fit)


def fitness_selected(original, selected, points):
    fit = 0
    for i in range(len(points)):
        r = original[points[i][0]][points[i][1]][0] - selected[points[i][0]][points[i][1]][0]
        g = original[points[i][0]][points[i][1]][1] - selected[points[i][0]][points[i][1]][1]
        b = original[points[i][0]][points[i][1]][2] - selected[points[i][0]][points[i][1]][2]
        fit += r*r + b*b + g*g
    return math.sqrt(fit)

