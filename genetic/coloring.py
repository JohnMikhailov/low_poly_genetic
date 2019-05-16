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
    max_color_value = 0
    max_color = None
    for i in range(xmin, xmax, 1):
        for j in range(ymin, ymax, 1):
            if tri.contains_point((i, j)):
                cur_count = color_count[pixels[i, j]]
                cur_color = pixels[i, j]
                if max_color_value < cur_count:
                    max_color_value = cur_count
                    max_color = cur_color
                color_count[cur_color] += 1
    return max_color
