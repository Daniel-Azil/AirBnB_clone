#!/usr/bin/python3

import json

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


    def all(self):
        """A custom method that returns dictionary attribute
           contained values and data.
        """
        return FileStorage.__objects

    def new(self, obj):
        """A custom method that places the key of the dict
           with name and ID of the object created.
        """
        class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}". format(class_name, obj.id)] = obj

    def save(self):
        """ A custom function that loads given object into JSONfile
        with specified path of the attrbute __file_path.
        """
        dictionary = {}
        filename = FileStorage.__file_path
        dict_object = FileStorage.__objects.items()
        for key_element, key_value in dict_object:
            dictionary[key_element] = key_value.to_dict()
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(dictionary, file)

    def reload(self):
        """ A custom method that reads data structure of the
            serialised JSON file in order to deserialise it.
        """
        try:
            filename = FileStorage.__file_path
            with open(filename, "r") as file:
                dsl_data_dict = json.load(file)
                for and_dict in dsl_data_dict.values():
                    name_of_class = and_dict["__class__"]
                    del and_dict["__class__"]
                    self.new(eval(name_of_class)(**and_dict))
        except FileNotFoundError:
            pass
