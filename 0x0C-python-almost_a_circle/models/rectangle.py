#!/usr/bin/python3
"""
This module implements a Rectangle object
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle implementation
    """

    def __init__(self, width: int, height: int, x=0, y=0, id=None):
        """initialization
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """string representation
        """
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.x, self.y, self.width, self.height)

    def check_type_value(self, name:  str, value: object, greater_equal=False):
        """type and value validation
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if not greater_equal:
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        else:
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self) -> int:
        """width getter
        """
        return self.__width

    @width.setter
    def width(self, width: int):
        """width setter
        """
        self.check_type_value('width', width)
        self.__width = width

    @property
    def height(self) -> int:
        """height getter
        """
        return self.__height
