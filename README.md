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

![Ryan Gosling](https://github.com/JohnMikhailov/low_poly_genetic/raw/master/images/gosling.jpg)

output1:

![Ryan Gosling low poly](https://github.com/JohnMikhailov/low_poly_genetic/raw/master/outputs/gosling.jpg)

As you can see eyes look pretty weird, because of points density in eyes erea

input2:
![mountains](https://github.com/JohnMikhailov/low_poly_genetic/raw/master/images/mount.jpg)

output2:
![mountains low poly](https://github.com/JohnMikhailov/low_poly_genetic/raw/master/outputs/mount.jpg)
