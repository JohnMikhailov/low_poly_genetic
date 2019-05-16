import random
from random import randint as rnd
from PIL import Image, ImageDraw
import numpy as np
import matplotlib.path as mp
from collections import defaultdict
from scipy.spatial import Delaunay


def color(polygon, pixels):
    tri = mp.Path(np.array(polygon))
    x = [int(polygon[point][0]) for point in range(len(polygon))]
    y = [int(polygon[point][1]) for point in range(len(polygon))]
    xmax = max(x)
    xmin = min(x)
    ymax = max(y)
    ymin = min(y)
    color_count = defaultdict(int)
    for i in range(xmin, xmax, 1):
        for j in range(ymin, ymax, 1):
            if tri.contains_point((i, j)):
                color_count[pixels[i, j]] += 1
    max_color = max(color_count.values() or [0])
    fill_color = None if max_color > 0 else pixels[xmax - 1, ymax - 1]
    for color_, count in color_count.items():
        if count == max_color:
            return color_
        fill_color = color_
    return fill_color
