from virus import Virus
import unittest

class TestVirusMetods(unittest.TestCase):

    def test_update(self):
        v = Virus()
        v.update(1.1)
        self.assertEqual(v.R0,1.1)