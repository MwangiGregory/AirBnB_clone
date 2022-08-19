#!/usr/bin/python3
"""This module defines class BaseModel"""
import uuid
from datetime import datetime


class BaseModel:
    """This class defines type BaseModel"""

    def __init__(self):
        """Constructor"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """return a string representation of instance of BaseModel"""
        return f"[{self.__class__.__name__}] ({self.id})"\
               f" {self.__dict__}"

    def save(self):
        """updates the public instance method updated_at
        with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary representaion of an instance of
        BaseModel"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
