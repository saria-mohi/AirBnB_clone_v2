#!/usr/bin/python3
"""Module to define the BaseModel Class"""
import uuid
import datetime as dt
import models


class BaseModel:
    """class that defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Base class constructor method

        Args:
            args: Received Tuple with parameters to initialize a new object
            kwargs: Recceived Dictionary with parameters to init a new object.
        """
        if kwargs is not None and len(kwargs) > 0:
            for key, v in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, dt.datetime.strptime(v,
                            '%Y-%m-%dT%H:%M:%S.%f'))
                elif key == "id":
                    self.id = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.datetime.now()
            self.updated_at = dt.datetime.now()
            models.storage.new(self)

    def save(self):
        """updates the public instance attribute updated_at with
        the current datetime.
        """
        self.updated_at = dt.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance.
        """
        myDict = self.__dict__.copy()
        myDict["__class__"] = self.__class__.__name__
        myDict["created_at"] = self.created_at.isoformat()
        myDict["updated_at"] = self.updated_at.isoformat()
        return myDict

    def __str__(self):
        """string representation of the created class.

        Return:
            format: [<class name>] (<self.id>) <self.__dict__>
        """
        string = "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__)
        return string

    def all(class_name):
        """Update your command interpreter
        (console.py) to retrieve all instances of
        a class by using: <class name>.all()
        """
        dir_obj = models.storage.all()
        my_list = []
        for obj_id in dir_obj.keys():
            if dir_obj[obj_id].__class__.__name__ == class_name:
                my_list.append(str(dir_obj[obj_id]))
        return my_list

    def count(class_name):
        """Update your command interpreter
        (console.py) to retrieve the number of
        instances of a class: <class name>.count()."""
        dir_obj = models.storage.all()
        n_elem = 0
        for obj_id in dir_obj.keys():
            if dir_obj[obj_id].__class__.__name__ == class_name:
                n_elem += 1
        return n_elem

    def show(class_name):
        """Update your command interpreter
        (console.py) to retrieve the number of
        instances of a class: <class name>.count()."""
        dir_obj = models.storage.all()
        args = class_name.split(',')
        for obj_id in dir_obj.keys():
            if dir_obj[obj_id].__class__.__name__ == args[0]\
               and dir_obj[obj_id].id == args[1]:
                return dir_obj[obj_id]
        return

    def destroy(class_name):
        """Update your command interpreter
        (console.py) to retrieve the number of
        instances of a class: <class name>.count()."""
        dir_obj = models.storage.all()
        args = class_name.split(',')
        key = "{}.{}".format(args[0], args[1])
        if key not in dir_obj.keys():
            print("** no instance found **")
        else:
            models.storage.delete(key)
        return
