#!/usr/bin/python3
"""
This module contains BaseModel that defines all common
attributes/methods for other classes.
"""
import re
from datetime import datetime, date, time
from uuid import uuid4

class BaseModel:
    """
    defines all common attributes/methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        """ Instance method"""
        
        if kwargs or len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    the_date = [int(i) for i in re.split("[-:.T]", str(value))]
                    self.__dict__[key] = datetime(
                        year=the_date[0],
                        month=the_date[1],
                        day=the_date[2],
                        hour=the_date[3],
                        second=the_date[4],
                        microsecond=the_date[5]
                    )
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ A nicely printable string representation of the
            object BaseModel
        """
        return "[BaseModel] ({:s}) {}".format(self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with
            the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of
            __dict__ of the instance
        """
        self.__dict__["__class__"] = "BaseModel"
        dict_copy = dict(self.__dict__)
        dict_copy['created_at'] = dict_copy['created_at'].isoformat()
        dict_copy['updated_at'] = dict_copy['updated_at'].isoformat()
        return dict_copy


if __name__ == "__main__":

    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)