import unittest
from counter_wrapper import CounterWrapper
from work_lamp import WorkLamp


class TestCounterWrapper(unittest.TestCase):

    def test_create(self):
        wrapper = CounterWrapper(WorkLamp())
        self.assertIsNotNone(wrapper)

    def test_counting(self):
        wrapper = CounterWrapper(WorkLamp())
        self.assertEqual(0, wrapper.count())

        wrapper.switch()
        self.assertEqual(1, wrapper.count())

        wrapper.switch()
        self.assertEqual(2, wrapper.count())

        wrapper.switch()
        self.assertEqual(3, wrapper.count())

        wrapper.switch()
        self.assertEqual(4, wrapper.count())

    def test_translating(self):
        lamp = WorkLamp()
        wrapper = CounterWrapper(lamp)

        wrapper.switch()
        self.assertTrue(wrapper.is_lighted())
        self.assertTrue(lamp.is_lighted())

        wrapper.switch()
        self.assertFalse(wrapper.is_lighted())
        self.assertFalse(lamp.is_lighted())

        wrapper.switch()
        self.assertTrue(wrapper.is_lighted())
        self.assertTrue(lamp.is_lighted())