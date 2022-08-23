#!/usr/bin/python3
"""This module defines class State"""
from models.base_model import BaseModel


class State(BaseModel):
    """This class defines a State"""
    name = ""

    def __init__(self, *args, **kwargs):
        """constructor"""
        super().__init__(*args, **kwargs)
