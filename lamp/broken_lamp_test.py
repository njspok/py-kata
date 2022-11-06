import unittest
from broken_lamp import BrokenLamp


class TestBrokenLamp(unittest.TestCase):

    def test_create(self):
        lamp = BrokenLamp(10)
        self.assertIsNotNone(lamp)

    def test_no_lighting(self):
        lamp = BrokenLamp(10)
        self.assertFalse(lamp.is_lighted())

        lamp.switch()
        self.assertFalse(lamp.is_lighted())

        lamp.switch()
        self.assertFalse(lamp.is_lighted())

    def test_lighting(self):
        lamp = BrokenLamp(3)
        self.assertFalse(lamp.is_lighted())

        for _ in range(10):
            # try 1
            lamp.switch()
            self.assertFalse(lamp.is_lighted())

            # try 2
            lamp.switch()
            self.assertFalse(lamp.is_lighted())

            # try 3
            lamp.switch()
            self.assertTrue(lamp.is_lighted())

    def test_hopelessly(self):
        lamp = BrokenLamp(0)
        self.assertFalse(lamp.is_lighted())

        for _ in range(10):
            lamp.switch()
            self.assertFalse(lamp.is_lighted())

    def test_working(self):
        lamp = BrokenLamp(1)
        self.assertFalse(lamp.is_lighted())

        for _ in range(10):
            lamp.switch()
            self.assertTrue(lamp.is_lighted())

            lamp.switch()
            self.assertFalse(lamp.is_lighted())


