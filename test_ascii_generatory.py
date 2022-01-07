import pytest
from asciigenerator import AsciiGenerator as ag

class TestAsciiGenerator:
    def __init__(self):
        self.path = '/pics/me_pic_hat_glass.jpeg'
        self.generator = ag(self.path)

    def test_image_resize(self):
        width = 150
        self.generator.image_resize(width)
        assert self.generator.IMAGE.size == (150, 150)

