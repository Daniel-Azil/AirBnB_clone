# # HBNB Project

The HBNB (Holberton's Airbnb) project is a Python-based project that aims to create a storage and console system for a simple Airbnb clone. It utilizes Python classes to manage and store objects.

## BaseModel

`BaseModel` is the base class for all other classes in the HBNB project. It provides the following functionality:

- Object creation with a unique ID.
- Automatic tracking of creation and update timestamps.
- Saving and updating objects in JSON files.

### Usage

```python
from models.base_model import BaseModel

# Create a new BaseModel instance
my_model = BaseModel()

# Access and modify attributes
my_model.name = "My First Model"
my_model.my_number = 89

# Save changes to a JSON file
my_model.save()

# Convert the object to a dictionary
my_model_json = my_model.to_dict()

## FileStorage
`FileStorage` is a storage engine used to save and load objects from JSON files. It offers the following features:

- Storing objects in dictionaries.
- Saving objects to a JSON file.
- Loading objects from a JSON file. 

### Usage

```python
from models.engine.file_storage import FileStorage

# Create a new FileStorage instance
storage = FileStorage()

# Load objects from a JSON file (if it exists)
storage.reload()

# Access the stored objects
objects_dict = storage.all()

# Save objects to a JSON file
storage.save()
