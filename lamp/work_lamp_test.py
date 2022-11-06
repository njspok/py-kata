import unittest
from work_lamp import WorkLamp


class TestWorkLamp(unittest.TestCase):

    def test_create(self):
        self.assertIsNotNone(WorkLamp())

    def test_is_lighted_off(self):
        lamp = WorkLamp()
        self.assertFalse(lamp.is_lighted())

    def test_switch(self):
        lamp = WorkLamp()
        self.assertFalse(lamp.is_lighted())

        # turn on
        lamp.switch()
        self.assertTrue(lamp.is_lighted())

        # turn off
        lamp.switch()
        self.assertFalse(lamp.is_lighted())

        # turn on
        lamp.switch()
        self.assertTrue(lamp.is_lighted())

