from settings import settings
from low_poly import low_poly

ga = settings[0]
canny = settings[1]

processed = low_poly('images/tiger.jpg', canny, ga)

processed.show()
processed.save('lp1.jpg')
