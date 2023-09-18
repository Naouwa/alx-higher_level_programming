#!/usr/bin/python3
""" Module for testing the Base class """
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


class TestBaseMethods(unittest.TestCase):
    """ Test suite for the Base class """

    def setUp(self):
        """ Method invoked before each test """
        Base._Base__nb_objects = 0

    def test_id(self):
        """ Test assigning an ID """
        base_instance = Base(1)
        self.assertEqual(base_instance.id, 1)

    def test_id_default(self):
        """ Test the default ID """
        base_instance = Base()
        self.assertEqual(base_instance.id, 1)

    def test_id_nb_objects(self):
        """ Test the 'nb_objects' attribute """
        base_instance1 = Base()
        base_instance2 = Base()
        base_instance3 = Base()
        self.assertEqual(base_instance1.id, 1)
        self.assertEqual(base_instance2.id, 2)
        self.assertEqual(base_instance3.id, 3)

    def test_id_mix(self):
        """ Test a mix of 'nb_objects' and assigned ID """
        base_instance1 = Base()
        base_instance2 = Base(1024)
        base_instance3 = Base()
        self.assertEqual(base_instance1.id, 1)
        self.assertEqual(base_instance2.id, 1024)
        self.assertEqual(base_instance3.id, 2)

    def test_string_id(self):
        """ Test using a string as ID """
        base_instance = Base('1')
        self.assertEqual(base_instance.id, '1')

    def test_more_args_id(self):
        """ Test passing extra arguments to the init method """
        with self.assertRaises(TypeError):
            base_instance = Base(1, 1)

    def test_access_private_attrs(self):
        """ Test accessing private attributes """
        base_instance = Base()
        with self.assertRaises(AttributeError):
            base_instance.__nb_objects

    def test_save_to_file_1(self):
        """ Test saving to a JSON file """
        Square.save_to_file(None)
        res = "[]\n"
        with open("Square.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)

        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_2(self):
        """ Test saving to a JSON file """
        Rectangle.save_to_file(None)
        res = "[]\n"
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)
        try:
            os.remove("Rectangle.json")
        except:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

if __name__ == '__main__':
    unittest.main()
