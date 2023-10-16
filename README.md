# # HBNB Project

The HBNB (Holberton's Airbnb) project is a Python-based project that aims to create a storage and console system for a simple Airbnb clone. It utilizes Python classes to manage and store objects.
- **create:** Create a new instance of a class and save it to a JSON file.
    ```python
    (hbnb) create BaseModel
    ```

- **show:** Display the details of a specific instance by providing the class name and instance ID.
    ```python
    (hbnb) show BaseModel 12345
    ```

- **destroy:** Remove an instance from the system using the class name and instance ID.
    ```python
    (hbnb) destroy BaseModel 12345
    ```

- **all:** List all instances of a class or all instances in the system.
    ```python
    (hbnb) all BaseModel
    ```

- **update:** Modify the attributes of an instance using the class name, instance ID, attribute name, and new value.
    ```python
    (hbnb) update BaseModel 12345 name "New Name"
    ```

- **count:** Count the number of instances of a specific class.
    ```python
    (hbnb) count BaseModel
    ```

- **quit/EOF:** Exit the HBNB console.

- **Unknown Commands:** The HBNB console handles unknown commands by trying to interpret them as specific actions, such as show, update, or destroy. If the format of the command is incorrect, an error message is displayed.

The HBNB console provides a flexible and interactive way to manage objects in the HBNB project. You can use it to create, view, update, and delete objects, making it a powerful tool for working with your Airbnb clone.

Feel free to explore and interact with the HBNB console to manage your HBNB objects efficiently.

To start the HBNB console, run the following command in your terminal:

```shell
$ ./console.py


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
```
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
```

## Place

The `Place` class represents accommodation places in the HBNB project. It has attributes like `city_id`, `user_id`, `name`, `description`, `number_rooms`, `number_bathrooms`, `max_guest`, `price_by_night`, `latitude`, `longitude`, and `amenity_ids`. It inherits from the `BaseModel` class.

### Usage

```python
from models.place import Place

# Create a new Place instance
my_place = Place()

# Set attributes
my_place.name = "Cozy Cabin"
my_place.number_rooms = 2
my_place.price_by_night = 100

# Save the place to a JSON file
my_place.save()

# Convert the object to a dictionary
my_place_json = my_place.to_dict()
```

## State
The `State` class represents states in the HBNB project. It has a single attribute, name, and inherits from the BaseModel class.

Usage
```python
from models.state import State

# Create a new State instance
my_state = State()

# Set the state's name
my_state.name = "California"

# Save the state to a JSON file
my_state.save()

# Convert the object to a dictionary
my_state_json = my_state.to_dict()
```

## User
The `User` class represents users in the HBNB project. It has attributes like email, password, first_name, and last_name. It inherits from the BaseModel class.

Usage
```python
from models.user import User

# Create a new User instance
my_user = User()

# Set user details
my_user.email = "user@example.com"
my_user.first_name = "John"
my_user.last_name = "Doe"

# Save the user to a JSON file
my_user.save()

# Convert the object to a dictionary
my_user_json = my_user.to_dict()
```

## City
The `City` class represents cities in the HBNB project. It has attributes state_id and name. It inherits from the BaseModel class.

Usage
```python
from models.city import City

# Create a new City instance
my_city = City()

# Set city attributes
my_city.state_id = "CA"
my_city.name = "San Francisco"

# Save the city to a JSON file
my_city.save()

# Convert the object to a dictionary
my_city_json = my_city.to_dict()
```

## Amenity
The `Amenity` class represents amenities available in accommodation places. It has a single attribute, name, and inherits from the BaseModel class.

Usage
```python
from models.amenity import Amenity

# Create a new Amenity instance
my_amenity = Amenity()

# Set amenity name
my_amenity.name = "Wi-Fi"

# Save the amenity to a JSON file
my_amenity.save()

# Convert the object to a dictionary
my_amenity_json = my_amenity.to_dict()
```

## Review
The `Review` class represents reviews for accommodation places. It has attributes place_id, user_id, and text. It inherits from the BaseModel class.

Usage
```python
Copy code
from models.review import Review

# Create a new Review instance
my_review = Review()

# Set review details
my_review.place_id = "12345"
my_review.user_id = "user123"
my_review.text = "Great place to stay!"

# Save the review to a JSON file
my_review.save()

# Convert the object to a dictionary
my_review_json = my_review.to_dict()
