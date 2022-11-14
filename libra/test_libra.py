import unittest

from libra import Libra


class TestLibra(unittest.TestCase):
    def test_balance(self):
        libra = Libra()
        self.assertEqual(0, libra.balance())
        self.assertEqual(0, libra.left())
        self.assertEqual(0, libra.right())
        
        libra.put(100)
        self.assertEqual(100, libra.balance())
        self.assertEqual(100, libra.left())
        self.assertEqual(0, libra.right())

        libra.put(200)
        self.assertEqual(100, libra.balance())
        self.assertEqual(100, libra.left())
        self.assertEqual(200, libra.right())

        libra.put(100)
        self.assertEqual(0, libra.balance())
        self.assertEqual(200, libra.left())
        self.assertEqual(200, libra.right())

        libra.put(400)
        self.assertEqual(400, libra.balance())
        self.assertEqual(600, libra.left())
        self.assertEqual(200, libra.right())

        libra.put(250)
        self.assertEqual(150, libra.balance())
        self.assertEqual(600, libra.left())
        self.assertEqual(450, libra.right())

        libra.put(50)
        self.assertEqual(100, libra.balance())
        self.assertEqual(600, libra.left())
        self.assertEqual(500, libra.right())

        libra.put(50)
        self.assertEqual(50, libra.balance())
        self.assertEqual(600, libra.left())
        self.assertEqual(550, libra.right())

    def test_invalid_value(self):
        libra = Libra()

        with self.assertRaises(ValueError):
            libra.put(-1)





