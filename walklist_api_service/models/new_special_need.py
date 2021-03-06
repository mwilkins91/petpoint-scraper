# coding: utf-8

"""
    The Enrichment List

    The THS enrichment list  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: contactme@markwilkins.co
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class NewSpecialNeed(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'name': 'str',
        'acronym': 'str',
        'priority': 'int',
        'color': 'str',
        'behaviours': 'list[int]',
        'animal_type': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'acronym': 'acronym',
        'priority': 'priority',
        'color': 'color',
        'behaviours': 'behaviours',
        'animal_type': 'animalType'
    }

    def __init__(self, id=None, name=None, acronym=None, priority=None, color=None, behaviours=None, animal_type=None):  # noqa: E501
        """NewSpecialNeed - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._acronym = None
        self._priority = None
        self._color = None
        self._behaviours = None
        self._animal_type = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        self.acronym = acronym
        self.priority = priority
        self.color = color
        if behaviours is not None:
            self.behaviours = behaviours
        self.animal_type = animal_type

    @property
    def id(self):
        """Gets the id of this NewSpecialNeed.  # noqa: E501


        :return: The id of this NewSpecialNeed.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NewSpecialNeed.


        :param id: The id of this NewSpecialNeed.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this NewSpecialNeed.  # noqa: E501


        :return: The name of this NewSpecialNeed.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NewSpecialNeed.


        :param name: The name of this NewSpecialNeed.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def acronym(self):
        """Gets the acronym of this NewSpecialNeed.  # noqa: E501


        :return: The acronym of this NewSpecialNeed.  # noqa: E501
        :rtype: str
        """
        return self._acronym

    @acronym.setter
    def acronym(self, acronym):
        """Sets the acronym of this NewSpecialNeed.


        :param acronym: The acronym of this NewSpecialNeed.  # noqa: E501
        :type: str
        """
        if acronym is None:
            raise ValueError("Invalid value for `acronym`, must not be `None`")  # noqa: E501

        self._acronym = acronym

    @property
    def priority(self):
        """Gets the priority of this NewSpecialNeed.  # noqa: E501


        :return: The priority of this NewSpecialNeed.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this NewSpecialNeed.


        :param priority: The priority of this NewSpecialNeed.  # noqa: E501
        :type: int
        """
        if priority is None:
            raise ValueError("Invalid value for `priority`, must not be `None`")  # noqa: E501

        self._priority = priority

    @property
    def color(self):
        """Gets the color of this NewSpecialNeed.  # noqa: E501


        :return: The color of this NewSpecialNeed.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this NewSpecialNeed.


        :param color: The color of this NewSpecialNeed.  # noqa: E501
        :type: str
        """
        if color is None:
            raise ValueError("Invalid value for `color`, must not be `None`")  # noqa: E501

        self._color = color

    @property
    def behaviours(self):
        """Gets the behaviours of this NewSpecialNeed.  # noqa: E501


        :return: The behaviours of this NewSpecialNeed.  # noqa: E501
        :rtype: list[int]
        """
        return self._behaviours

    @behaviours.setter
    def behaviours(self, behaviours):
        """Sets the behaviours of this NewSpecialNeed.


        :param behaviours: The behaviours of this NewSpecialNeed.  # noqa: E501
        :type: list[int]
        """

        self._behaviours = behaviours

    @property
    def animal_type(self):
        """Gets the animal_type of this NewSpecialNeed.  # noqa: E501


        :return: The animal_type of this NewSpecialNeed.  # noqa: E501
        :rtype: int
        """
        return self._animal_type

    @animal_type.setter
    def animal_type(self, animal_type):
        """Sets the animal_type of this NewSpecialNeed.


        :param animal_type: The animal_type of this NewSpecialNeed.  # noqa: E501
        :type: int
        """
        if animal_type is None:
            raise ValueError("Invalid value for `animal_type`, must not be `None`")  # noqa: E501

        self._animal_type = animal_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(NewSpecialNeed, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NewSpecialNeed):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
