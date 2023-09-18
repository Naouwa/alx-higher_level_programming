#!/usr/bin/python3
""" Module for testing the Square class """
import unittest
from io import StringIO
from unittest.mock import patch
from models.square import Square
from models.base import Base

class TestSquareMethods(unittest.TestCase):
    """ Suite to test the Square class """

    def setUp(self):
        """ Method invoked before each test to reset the object count """
        Base._Base__nb_objects = 0

    def test_new_square(self):
        """ Test creating a new square and checking its attributes """
        new = Square(3)
        self.assertEqual(new.size, 3)
        self.assertEqual(new.width, 3)
        self.assertEqual(new.height, 3)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_new_square_2(self):
        """ Test creating a new square with all attributes """
        new = Square(2, 5, 5, 4)
        self.assertEqual(new.size, 2)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 2)
        self.assertEqual(new.x, 5)
        self.assertEqual(new.y, 5)
        self.assertEqual(new.id, 4)

    def test_incorrect_amount_attrs(self):
        """ Test error raised with no arguments passed """
        with self.assertRaises(TypeError):
            new = Square()

    def test_incorrect_amount_attrs_1(self):
        """ Test error raised with too many arguments passed """
        with self.assertRaises(TypeError):
            new = Square(1, 1, 1, 1, 1)

    def test_access_private_attrs(self):
        """ Trying to access a private attribute """
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__width

    def test_access_private_attrs_2(self):
        """ Trying to access a private attribute """
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__height

    def test_access_private_attrs_3(self):
        """ Trying to access a private attribute """
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__x

    def test_access_private_attrs_4(self):
        """ Trying to access a private attribute """
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__y

    def test_area(self):
        """ Checking the return value of the area method """
        new = Square(4)
        self.assertEqual(new.area(), 16)

    def test_load_from_file(self):
        """ Test loading from JSON file """
        load_file = Square.load_from_file()
        self.assertEqual(load_file, load_file)

    def test_display(self):
        """ Test the string printed by the display method """
        r1 = Square(2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_str(self):
        """ Test __str__ return value """
        r1 = Square(4, 2, 2)
        res = "[Square] (1) 2/2 - 4\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_json_file(self):
        """ Test saving and loading JSON file """
        s1 = Square(2)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        res = "[{}]\n".format(dictionary.__str__())
        res = res.replace("'", "\"")

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
            self.assertEqual(str_out.getvalue(), res)

        Square.save_to_file([s1])
        res = "[{}]".format(dictionary.__str__())
        res = res.replace("'", "\"")

        with open("Square.json", "r") as file:
            res2 = file.read()

        self.assertEqual(res, res2)

    def test_create(self):
        """ Test create method """
        dictionary = {'id': 89}
        s1 = Square.create(**dictionary)
        self.assertEqual(s1.id, 89)

if __name__ == "__main__":
    unittest.main()
