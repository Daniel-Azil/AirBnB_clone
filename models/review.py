#!/usr/bin/python3

"""
    A module that contains the class named Review.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
        A class that contains public attributes initialised
        and inherited by the BaseModel class from
        model/base_model.py
    """
    place_id = ""
    user_id = ""
    text = ""
