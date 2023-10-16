#!/usr/bin/python3

"""
    A module that intialises the class named State that
    inherits from the class named BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
        A class that inherits from BaseModel class in
        model/base_model.py file to set in the name of the
        city and specific id for each city created in
        relation to the assigned state.
    """
    state_id = ""
    name = ""
