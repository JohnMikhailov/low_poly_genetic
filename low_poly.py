from PIL import Image, ImageDraw
import numpy as np
from scipy.spatial import Delaunay
from collections import defaultdict
import cv2
from smoothing.smooth import Smooth


def color(polygon, pixels):
    x = [int(polygon[point][0]) for point in range(len(polygon))]
    y = [int(polygon[point][1]) for point in range(len(polygon))]
    xmax = max(x)
    xmin = min(x)
    ymax = max(y)
    ymin = min(y)
    color_count = defaultdict(int)
    for i in range(xmin, xmax, 1):
        for j in range(ymin, ymax, 1):
            color_count[pixels[i, j]] += 1
    max_color = max(color_count.values() or [0])
    fill_color = None
    for key in color_count:
        fill_color = key
        if color_count[key] == max_color:
            return key
    return fill_color


def low_poly(original, settings):
    ga, canny = settings[0], settings[1]
    image = Image.open(original)
    processed = Image.open(original)
    pixels = image.load()
    layer = Image.new('RGBA', image.size)
    draw = ImageDraw.Draw(layer)

    lower, upper = canny['lower'], canny['upper']
    edges = cv2.Canny(cv2.imread(original), lower, upper)

    smooth = Smooth(edges, ga['gens_amount'], ga['threshold'], ga['fitness'], ga['radius'])
    smooth.start(ga['start_method']['generations'], ga['start_method']['use_fitness'])
    points = smooth.get_binary()

    non_zero_indices = np.where(points > 0)
    points = list(zip(non_zero_indices[1], non_zero_indices[0]))

    tri = Delaunay(points)
    for i in tri.simplices:
        poly = [tuple(points[i[j]]) for j in (0, 1, 2)]
        draw.polygon(poly, fill=color(poly, pixels))
    processed.paste(layer, mask=layer)
    return processed
