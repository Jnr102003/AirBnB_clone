#!/usr/bin/python3
"""
Defines amenities
This is a simple implementation of the Amenity class, 
which inherits from the BaseModel class. 
The Amenity class only has one attribute, a name attribute, 
which represents the name of the amenity. This class is designed 
to represent amenities that can be offered at a user's place, such 
as a swimming pool, gym, or free parking. The name attribute is a 
string that represents the name of the amenity.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines amenities that user can choose from to offer at its place"""
    name = ""
