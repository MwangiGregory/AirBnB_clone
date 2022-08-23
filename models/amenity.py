#!/usr/bin/python3
"""This module defines class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class defines an Amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """constructor"""
        super().__init__(*args, **kwargs)
