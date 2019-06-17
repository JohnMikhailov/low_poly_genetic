This algorithm creates new image with low-poly design.
For now it's not work so well, but you can use it just for fun.
To run algorithm, create empty python-file and use function low_poly() from low_poly package.
Also you have to import settings file, where you can add your settings - this is used to make changes in oupputs.

Example:

from settings import settings
from low_poly import low_poly

input_path = 'images/tiger.jpg'
processed = low_poly(input_path, settings)
processed.show()

![Image alt](https://github.com/{JohnMikhailov}/{low_poly_genetic}/raw/{master}/{outputs}/gosling.jpg)
