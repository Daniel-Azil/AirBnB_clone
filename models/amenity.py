#!/usr/bin/python3

"""
    A module that indicates the amenities that are available
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        A custom class that sets the amenities through the
        class attributes inherited by BaseModel class
        in models/base_model.py file.
    """
    name = ""
