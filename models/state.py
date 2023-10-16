#!/usr/bin/python3

"""
    A custom module that contains the class named State
    that inherits from BaseModel class.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
        A class that inherits from the class named BaseModel
        to set the name of given states with the class
        attribute named state.
    """
    name = ""
