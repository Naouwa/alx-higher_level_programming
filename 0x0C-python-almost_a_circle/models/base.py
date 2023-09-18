#!/usr/bin/python3
"""Creating a Base Class"""
import json
import os


class Base:
    """The Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializing class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """A standard formats for sharing data representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that writes the JSON string
        representation of list_objs to a file
        """
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            list_objs = []
        dicList = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(dicList))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """A class method that returns a list of instances"""
        filename = "{}.json".format(cls.__name__)
        if os.path.isfile(filename):
            with open(filename, "r", encoding="utf-8") as f:
                json_data = f.read()
                if json_data:
                    return [cls.create(**val) for val in
                            cls.from_json_string(json_data)]
                return []
