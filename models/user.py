#!/usr/bin/python3

""" A custom Module that contains the class named User.
    The class is used in assigning the names, email and
    password of the a specified user.
"""

import json
from models.base_model import BaseModel


class User(BaseModel):
    """
        A custom class that assigns the user first name,
        last name, email, and password as class attributes
        inheriting from the BaseModel class in base_model.py
        file.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
