import unittest
from models.square import Square


class TestSquareClassMethods(unittest.TestCase):
    def test_contructor(self):
        square = Square(6, 3, 4, 2)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_size_property(self):
        square = Square(6, 3, 4, 2)
        self.assertEqual(square.size, 6)

    def test_size_property_setter(self):
        square = Square(6, 3, 4, 2)
        square.size = 8
        self.assertEqual(square.area(), 8)

    def test_update_args(self):
        square = Square(6, 3, 4, 2)
        square.update(3, 8, 9, 5)
        self.assertEqual(square.id, 3)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 9)
        self.assertEqual(square.y, 5)

    def test_update_kwargs(self):
        square = Square(6, 3, 4, 2)
        square.update(id=3, size=8, x=9, y=5)
        self.assertEqual(square.id, 3)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 9)
        self.assertEqual(square.y, 5)

    def test_to_dictionary(self):
        square = Square(6, 3, 4, 2)
        expected_dict = {
                "id": 2,
                "size": 6,
                "x": 3,
                "y": 4
        }
        self.assertEqual(square.to_dictionary(), expected_dict)

if __name__ == "__main__":
    unittest.main()
