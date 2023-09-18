import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square



class TestBaseClassMethods(unittest.TestCase):
    def test_to_json_string(self):
        data = [{"key1": "value1"}, {"key2": "value2"}]
        json_string = Base.to_json_string(data)
        self.assertIsInstance(json_string, str)
        self.assertEqual(json_string, '[{"key1": "value1"}, {"key2": "value2"}]')

    def test_from_json_string(self):
        json_string = '[{"key1": "value1"}, {"key2": "value2"}]'
        data = Base.from_json_string(json_string)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["key1"], "value1")
        self.assertEqual(data[1]["key2"], "value2")

    def test_save_to_file(self):
        filename = "test_save.json"
        data = [{"key1": "value1"}, {"key2": "value2"}]
        Base.save_to_file(data)
        self.assertTrue(os.path.isfile(filename))
        os.remove(filename)

   """ def test_create(self):
        data = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        dummy = Rectangle.create(**data)
        self.assertIsInstance(dummy, Base)
        self.assertEqual(dummy.key1, "value1")
        self.assertEqual(dummy.key2, "value2")"""

    def test_create(self):
        data = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        dummy = Rectangle.create(**data)
        self.assertIsInstance(dummy, Rectangle)
        self.assertEqual(dummy.id, 1)
        self.assertEqual(dummy.width, 2)
        self.assertEqual(dummy.height, 3)
        self.assertEqual(dummy.x, 4)
        self.assertEqual(dummy.y, 5)

   """ def test_load_from_file(self):
        filename = "test_load.json"
        data = [{"key1": "value1"}, {"key2": "value2"}]
        Base.save_to_file(data)
        instances = Base.load_from_file()
        self.assertIsInstance(instances, list)
        self.assertEqual(len(instances), 2)
        self.assertEqual(instances[0].key1, "value1")
        self.assertEqual(instances[1].key2, "value2")
        os.remove(filename)"""

    def test_load_from_file(self):
        filename = "test_load.json"
        data = [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
                {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]
        Base.save_to_file(data)
        instances = Rectangle.load_from_file()
        self.assertIsInstance(instances, list)
        self.assertEqual(len(instances), 2)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[1].width, 7)
        self.assertEqual(instances[0].x, 4)
        self.assertEqual(instances[1].y, 10)
        os.remove(filename)

if __name__ == "__main__":
    unittest.main()
