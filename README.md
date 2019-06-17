This algorithm creates new image with low-poly design.
For now it's not work so well, but you can use it just for fun.
To run algorithm, create empty python-file and use function low_poly() from low_poly package.
Also you have to import settings file, where you can add your settings - this is used to make changes in oupputs.

# Code example

from settings import settings
from low_poly import low_poly

input_path = 'images/tiger.jpg'
processed = low_poly(input_path, settings)
processed.show()


# Outputs examples

input1:

![mountains](https://github.com/JohnMikhailov/low_poly_genetic/raw/master/images/mount.jpg)

output1:

![mountains low poly](https://github.com/JohnMikhailov/low_poly_genetic/raw/master/outputs/mount.jpg)

As you can see some areas of image is not covered by polygons: there is just more points than in other places on image.
You cannot see expicit polygons because of high density of points in those areas and in those areas appears a lot of small polygons - this leads to maximum approximation to original image at those areas.

As i already said - project is not work as well.
I made it becasue i wanted to see how genetic algorithm works with images.
