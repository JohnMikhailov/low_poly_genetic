class Settings:

    def __init__(self):

        self.colorspace_RGBA = 'RGBA'
        self.colorspace_RGB = 'RGB'

    def defaults(self):
        return {'color_space': self.colorspace_RGB, 'alpha': self.colorspace_RGBA}
