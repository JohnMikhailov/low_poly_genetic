from settings import settings
from low_poly import low_poly

processed = low_poly('images/tiger.jpg', settings)

processed.show()
processed.save('lp1.jpg')
