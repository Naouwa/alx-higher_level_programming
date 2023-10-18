#!/usr/bin/python3
""" Module for test Rectangle class """
import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleMethods(unittest.TestCase):
    """ Suite to test Rectangle class """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_new_rectangle(self):
        """ Test new rectangle """
        new_rect = Rectangle(1, 1)
        self.assertEqual(new_rect.width, 1)
        self.assertEqual(new_rect.height, 1)
        self.assertEqual(new_rect.x, 0)
        self.assertEqual(new_rect.y, 0)
        self.assertEqual(new_rect.id, 1)

    def test_new_rectangle_2(self):
        """ Test new rectangle with all attrs """
        new_rect = Rectangle(2, 3, 5, 5, 4)
        self.assertEqual(new_rect.width, 2)
        self.assertEqual(new_rect.height, 3)
        self.assertEqual(new_rect.x, 5)
        self.assertEqual(new_rect.y, 5)
        self.assertEqual(new_rect.id, 4)

    def test_new_rectangles(self):
        """ Test new rectangles """
        new_rect = Rectangle(1, 1)
        new_rect2 = Rectangle(1, 1)
        self.assertEqual(False, new_rect is new_rect2)
        self.assertEqual(False, new_rect.id == new_rect2.id)

    def test_is_Base_instance(self):
        """ Test Rectangle is a Base instance """
        new_rect = Rectangle(1, 1)
        self.assertEqual(True, isinstance(new_rect, Base))

    def test_incorrect_amount_attrs(self):
        """ Test error raise with 1 arg passed """
        with self.assertRaises(TypeError):
            new_rect = Rectangle(1)

    def test_area_2(self):
        """ Checking the return value of area method """
        new_rect = Rectangle(4, 5)
        self.assertEqual(new.area(), 20)

    def test_display(self):
        """ Test string printed """
        r1 = Rectangle(2, 5)
        res = "##\n##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_str(self):
        """ Test __str__ return value """
        r1 = Rectangle(2, 5, 2, 4)
        res = "[Rectangle] (1) 2/4 - 2/5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary(self):
        """ Test dictionary returned """
        r1 = Rectangle(1, 2, 3, 4, 1)
        res = "[Rectangle] (1) 3/4 - 1/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 1)

        res = "<class 'dict'>\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(r1.to_dictionary()))
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary_2(self):
        """ Test dictionary returned """
        r1 = Rectangle(2, 2, 2, 2)
        res = "[Rectangle] (1) 2/2 - 2/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r2 = Rectangle(5, 7)
        res = "[Rectangle] (2) 0/0 - 5/7\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r2)
            self.assertEqual(str_out.getvalue(), res)

        r1_dictionary = r1.to_dictionary()
        r2.update(**r1_dictionary)

        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)
        self.assertEqual(r1.id, r2.id)

if __name__ == '__main__':
    unittest.main()
