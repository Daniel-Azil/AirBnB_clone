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
        Initialised the constructor for the base model class containing
        attributes to be used
        by other methods and classes.

        Args:
            *args: unspecified range of arguments passed to parameter.
            **kwargs: unspecified range of key=value arguments passed
                      to parameter.
        """
        if kwargs:
            for key_ele, key_val in kwargs.items():
                if "created_at" == key_ele:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == key_ele:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == key_ele:
                    pass
                else:
                    setattr(self, key_ele, key_val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """
        A custom method that updates the public instance
        attributes named "updated_at" with
        the actual current date and time.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        A custom method that converts the deserialised datetime
        value of srtpdate to iso string format.
        """

        datetime_iso = {}
        datetime_iso["__class__"] = self.__class__.__name__
        for key_element, key_value in self.__dict__.items():
            if isinstance(key_value, datetime):
                datetime_iso[key_element] = key_value.isoformat()
            else:
                datetime_iso[key_element] = key_value
        return datetime_iso

    def __str__(self):
        """
        A method that prints the name of the instance of the
        class created, the id of the
        object created and the dict argument.
        """
        return ("[{}] ({}) {}". format(self.__class__.__name__,
                                       self.id, self.__dict__))

    def __repr__(self):
        """ A method that returns __str__ """
        return (self.__str__())
