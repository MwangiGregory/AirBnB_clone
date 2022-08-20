#!/urs/bin/python3
"""This module defines class FileStorage"""
import os
import json
from models.base_model import BaseModel


class FileStorage:
    """This class defines a file storage system"""
    __file_path = os.getcwd() + "/file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Adds obj to the dictionary __objects with
        a key with the format <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes the dictionary __objects to a file
        specified in __file_path"""
        # TODO check if obj is of type or subtype of class
        # BaseModel

        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes a json string from a json file to a
        dictionary __objects"""
        new_dict = {}
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                new_dict = json.load(f)
        except FileNotFoundError:
            pass
        else:
            for key, obj_dict in new_dict.items():
                obj_str = obj_dict['__class__'] + '(**obj_dict)'
                obj = eval(obj_str)
                self.__objects[key] = obj
