import random
from random import randint as rnd
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
import matplotlib.path as mp
from scipy.spatial import Delaunay
from scipy import ndimage, misc
from collections import defaultdict
import cv2
import time
import genetic.coloring
from smoothing.smooth import Smooth


def color(polygon, pixels):
    # tri = mp.Path(np.array(polygon))
    x = [int(polygon[point][0]) for point in range(len(polygon))]
    y = [int(polygon[point][1]) for point in range(len(polygon))]
    xmax = max(x)
    xmin = min(x)
    ymax = max(y)
    ymin = min(y)
    color_count = defaultdict(int)
    for i in range(xmin, xmax, 1):
        for j in range(ymin, ymax, 1):
            # if tri.contains_point((i, j)):
            color_count[pixels[i, j]] += 1
    max_color = max(color_count.values() or [0])
    # fill_color = None if max_color > 0 else pixels[xmax - 1, ymax - 1]
    fill_color = None
    for key in color_count:
        fill_color = key
        if color_count[key] == max_color:
            return key
    return fill_color


def draw_triangles(inp, image, saved, points_amount=0):
    width, height = image.size
    pixels = saved.load()
    layer = Image.new('RGBA', (width, height))
    layer_draw = ImageDraw.Draw(layer)
    # key_points = [(0, 0), (0, height), (width, 0), (width, height)]
    # points = key_points + [(rnd(0, width), rnd(0, height)) for _ in range(points_amount)]
    points = inp
    tri = Delaunay(points)
    for i in tri.simplices:
        a = tuple(points[i[0]])
        b = tuple(points[i[1]])
        c = tuple(points[i[2]])
        fill = color([a, b, c], pixels)
        layer_draw.polygon([a, b, c], fill=fill)
    image.paste(layer, mask=layer)
    image.show()


imp = 'images/paris.jpg'
image = Image.open(imp)
im = cv2.imread(imp)

edges = cv2.Canny(im, 100, 200)
Image.fromarray(edges).show()


s = Smooth(edges, 5000, (0.1, 0.5), fit=0.5, radius=5)
s.start(10)
r = s.get_binary()

Image.fromarray(r).show()

non_zero_indices = np.where(r > 0)
points = list(zip(non_zero_indices[1], non_zero_indices[0]))

saved = Image.open(imp)
draw_triangles(points, image, saved)

