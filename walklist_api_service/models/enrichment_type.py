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


class EnrichmentType(object):
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
        'animal_type': 'AnimalType'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'animal_type': 'animalType'
    }

    def __init__(self, id=None, name=None, animal_type=None):  # noqa: E501
        """EnrichmentType - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._animal_type = None
        self.discriminator = None
        self.id = id
        self.name = name
        self.animal_type = animal_type

    @property
    def id(self):
        """Gets the id of this EnrichmentType.  # noqa: E501


        :return: The id of this EnrichmentType.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EnrichmentType.


        :param id: The id of this EnrichmentType.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this EnrichmentType.  # noqa: E501


        :return: The name of this EnrichmentType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnrichmentType.


        :param name: The name of this EnrichmentType.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def animal_type(self):
        """Gets the animal_type of this EnrichmentType.  # noqa: E501


        :return: The animal_type of this EnrichmentType.  # noqa: E501
        :rtype: AnimalType
        """
        return self._animal_type

    @animal_type.setter
    def animal_type(self, animal_type):
        """Sets the animal_type of this EnrichmentType.


        :param animal_type: The animal_type of this EnrichmentType.  # noqa: E501
        :type: AnimalType
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
        if issubclass(EnrichmentType, dict):
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
        if not isinstance(other, EnrichmentType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
