#!/usr/bin/python3
"""This module defines class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class defines a Review"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """constructor"""
        super().__init__(*args, **kwargs)
