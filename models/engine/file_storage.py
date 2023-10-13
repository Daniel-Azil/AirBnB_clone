#!/usr/bin/python3

import json
from models.base_model import BaseModel

"""
    A custom Module that saves and modify new serialised
    objects into  JSON files for storage.
"""


class FileStorage:
    """
        A custome class that serialises, saves, modifies
        deserialises data structures in JSON files for
        storage functionalities.
    """
    __file_path = 'file.json'
    __objects = {}
    class_dict = {"BaseModel": BaseModel}


    def all(self):
        """A custom method that returns dictionary attribute
           contained values and data.
        """
        return self.__objects

    def new(self, obj):
        """A custom method that places the key of the dict
           with name and ID of the object created.
        """
        name_id = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[name_id] = obj

    def save(self):
        """ A custom function that loads given object into JSONfile
        with specified path of the attrbute __file_path.
        """
        dictionary = {}
        for key_element, key_value in self.__objects.items():
            dictionary[key_element] = key_value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(dictionary, file)

    def reload(self):
        """ A custom method that reads data structure of the
            serialised JSON file in order to deserialise it.
        """
        try:
            with open(self.__file_path, "r") as file:
                dsl_data_dict = json.load(file)
                for key_element, key_value in dsl_data_dict.items():
                    name_of_class = self.class_dict[key_value["__class__"]](**key_value)
                    self.__objects[key_element] = name_of_class
        except FileNotFoundError:
            pass
