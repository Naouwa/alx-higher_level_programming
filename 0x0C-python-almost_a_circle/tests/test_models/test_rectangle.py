import unittest
from models.rectangle import Rectangle


class TestRectangleClassMethods(unittest.TestCase):
    def test_area(self):
        rect = Rectangle(6, 12)
        self.assertEqual(rect.area(), 72)

    def test_display(self):
        rect = Rectangle(4, 3)
        expected_output = "####\n###\n"
        with captured_output() as (out, _):
            rect.display()
        self.assertEqual(str(rect), expected_output)

    def test_update(self):
        rect = Rectangle(5, 4, 2, 3, 8)
        rect.update(11, 6, 5)
        self.assertEqual(rect.id, 11)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 5)

    def test_to_dictionary(self):
        rect = Rectangle(5, 4, 2, 3, 8)
        expected_dict = {
                "id": 8,
                "width": 5,
                "height": 4,
                "x": 2,
                "y": 3
        }
        self.assertEqual(rect.to_dictionary(), expected_dict)

if __name__ == "__main__":
    unittest.main()

