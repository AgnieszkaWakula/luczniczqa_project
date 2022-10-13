import unittest


class TestABC(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("I'm setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("I'm tearDowanClass")

    def setUp(self) -> None:
        print("I'm setUp")

    def tearDown(self) -> None:
        print("I'm tearDown")

 #   def test_1
