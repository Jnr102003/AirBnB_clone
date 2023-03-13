#!/usr/bin/python3
"""Defines the BaseModel class."""
from models import storage
import uuid
from datetime import datetime

class BaseModel():
    """a class that defines base model
    """

    def __init__(self, *args, **kwargs):
        """
        This method takes *args and **kwargs as arguments, 
        which allows it to accept both positional and keyword arguments. 
        It sets the id, created_at, and updated_at attributes if they are 
        not provided as keyword arguments. If the attributes are provided as 
        keyword arguments, their values are converted to datetime objects using strptime.
        
        Attributes
        id: a string assigned with uuid instance
        created_at: current datetime of an instance
        updated_at: current datetime of an instance
        that is updated when a new object is created
        *args: not used if kwargs is empty
        **kwargs: key/ value pairs of the attributes
        date_format: time format
        """
        date_format = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    """
                    created_at and updated_at is changed to
                    date time object using strptime
                    """
                    value = datetime.strptime(kwargs[key], date_format)

                elif key == "__class__":
                    continue

                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """
        This method updates the updated_at attribute 
        of the instance to the current date and time using 
        datetime.now() and saves the instance to the storage 
        using the storage.save() method.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        This method returns a dictionary containing 
        all the attributes (keys and values) of the instance, 
        as well as the __class__ attribute. The created_at 
        and updated_at attributes are converted to ISO format 
        using isoformat().

        Attributes
        created_at: the isoformat of the current datetime
        updated_at: the isoformat of the current datetime
        new_dict: a dictionary containing keys and values
        __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict

    def __str__(self):
        """
        This method returns a string representation of the instance, 
        which includes the class name, id, and the contents of the __dict__ 
        attribute of the instance, thus, returns a string of the class name
        id and contents of the dictionary
        """
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
