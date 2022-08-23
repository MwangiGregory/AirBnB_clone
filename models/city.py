#!/usr/bin/python3
"""This module defines class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """This class defines a City"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """constructor"""
        super().__init__(*args, **kwargs)
