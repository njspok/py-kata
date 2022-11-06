import unittest
from man import Man, LampNotWorkingError
from work_lamp import WorkLamp
from counter_wrapper import CounterWrapper
from broken_lamp import BrokenLamp


class TestMan(unittest.TestCase):

    def test_create(self):
        man = Man(1)
        self.assertIsNotNone(man)

    def test_light_on(self):
        man = Man(1)

        lamp = WorkLamp()
        self.assertFalse(lamp.is_lighted())

        # light on
        man.light_on(lamp)
        self.assertTrue(lamp.is_lighted())

        # already lighted
        man.light_on(lamp)
        self.assertTrue(lamp.is_lighted())

    def test_already_lighted(self):
        man = Man(1)

        lamp = WorkLamp()
        lamp.switch()
        self.assertTrue(lamp.is_lighted())

        man.light_on(lamp)
        self.assertTrue(lamp.is_lighted())

    def test_impatient(self):
        man = Man(0)

        lamp = CounterWrapper(BrokenLamp(10))

        # only 1 attempt
        with self.assertRaises(LampNotWorkingError):
            man.light_on(lamp)

        self.assertEqual(1, lamp.count())

    def test_patient(self):
        man = Man(5)
        lamp = CounterWrapper(BrokenLamp(10))

        # trying
        with self.assertRaises(LampNotWorkingError):
            man.light_on(lamp)

        self.assertEqual(6, lamp.count())

    def test_lucky(self):
        man = Man(5)
        lamp = CounterWrapper(BrokenLamp(3))
        man.light_on(lamp)
        self.assertEqual(3, lamp.count())
