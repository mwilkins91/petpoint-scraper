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


class MultipleAnimalTypeResponse(object):
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
        'payload': 'list[AnimalType]'
    }

    attribute_map = {
        'payload': 'payload'
    }

    def __init__(self, payload=None):  # noqa: E501
        """MultipleAnimalTypeResponse - a model defined in Swagger"""  # noqa: E501
        self._payload = None
        self.discriminator = None
        if payload is not None:
            self.payload = payload

    @property
    def payload(self):
        """Gets the payload of this MultipleAnimalTypeResponse.  # noqa: E501


        :return: The payload of this MultipleAnimalTypeResponse.  # noqa: E501
        :rtype: list[AnimalType]
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this MultipleAnimalTypeResponse.


        :param payload: The payload of this MultipleAnimalTypeResponse.  # noqa: E501
        :type: list[AnimalType]
        """

        self._payload = payload

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
        if issubclass(MultipleAnimalTypeResponse, dict):
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
        if not isinstance(other, MultipleAnimalTypeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
