#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
import models

""" A module that defines the base model for all common attributes and methods
    for other classes
"""

class BaseModel():
    """
    A class that defines the base model for containing attributes to be used by
    other classes and methods.
    """
    
    def __init__(self, *args, **kwargs):
        """
        Initialised the constructor for the base model class containing attributes to be used
        by other methods and classes.

        Args:
            *args: unspecified range of arguments passed to parameter.
            **kwargs: unspecified range of key=value arguments passed to parameter.
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        strp_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs is not None or len(kwargs) != 0:
            for key_element, key_value in kwargs.items():
                if key_element == "created_at" or key_element == "updated_at":
                    self.__dict__[key_element] = datetime.strptime(key_value, strp_format)
                else:
                    self.__dict__[key_element] = key_value
        else:
            models.storage.new(self)
        

    def save(self):
        """
        A custom method that updates the public instance
        attributes named "updated_at" with
        the actual current date and time.
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        A custom method that converts the deserialised datetime
        value of srtpdate to iso string format.
        """

        datetime_iso = self.__dict__.copy()
        datetime_iso["created_at"] = self.created_at.isoformat()
        datetime_iso["updated_at"] = self.updated_at.isoformat()
        datetime_iso["__class__"] = self.__class__.__name__
        return datetime_iso


    def __str__(self):
        """
        A method that prints the name of the instance of the
        class created, the id of the
        object created and the dict argument.
        """
        return "[{}] ({}) {}". format(self.__class__.__name__, self.id, self.__dict__)
