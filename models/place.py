#!/usr/bin/python3

"""
    A Module containing a class that inherits from BaseModel
    from models/base_model.py file
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
        A class that inherits from BaseModel and setting the
        class attributes that sets the value object of each
        class object to the BaseModel.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_roomes = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
