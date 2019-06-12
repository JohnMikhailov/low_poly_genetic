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


def draw_triangles(inp, image, saved, output):
    width, height = image.size
    pixels = saved.load()
    layer = Image.new('RGBA', (width, height))
    layer_draw = ImageDraw.Draw(layer)
    points = inp
    tri = Delaunay(points)
    for i in tri.simplices:
        a = tuple(points[i[0]])
        b = tuple(points[i[1]])
        c = tuple(points[i[2]])
        fill = color([a, b, c], pixels)
        layer_draw.polygon([a, b, c], fill=fill)
    image.paste(layer, mask=layer)
    image.save(output)


im = Image.open('images/tiger.jpg')
saved = Image.open('images/tiger.jpg')
w, h = im.size
points = [(rnd(0, w), rnd(0, h)) for _ in range(5_000)]
draw_triangles(points, im, saved, 'outputs/tiger_triang.jpg')
