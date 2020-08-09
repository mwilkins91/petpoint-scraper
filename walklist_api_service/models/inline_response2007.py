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

def getResponse():
    from walklist_api_service.models.response import Response
    return Response

class InlineResponse2007(object):
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
        'payload': 'AnimalType',
        'meta': 'ResponseMeta'
    }
    if hasattr(getResponse(), "swagger_types"):
        swagger_types.update(getResponse().swagger_types)

    attribute_map = {
        'payload': 'payload',
        'meta': 'meta'
    }
    if hasattr(getResponse(), "attribute_map"):
        attribute_map.update(getResponse().attribute_map)

    def __init__(self, payload=None, meta=None, *args, **kwargs):  # noqa: E501
        """InlineResponse2007 - a model defined in Swagger"""  # noqa: E501
        self._payload = None
        self._meta = None
        self.discriminator = None
        if payload is not None:
            self.payload = payload
        if meta is not None:
            self.meta = meta
        Response.__init__(self, *args, **kwargs)

    @property
    def payload(self):
        """Gets the payload of this InlineResponse2007.  # noqa: E501


        :return: The payload of this InlineResponse2007.  # noqa: E501
        :rtype: AnimalType
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this InlineResponse2007.


        :param payload: The payload of this InlineResponse2007.  # noqa: E501
        :type: AnimalType
        """

        self._payload = payload

    @property
    def meta(self):
        """Gets the meta of this InlineResponse2007.  # noqa: E501


        :return: The meta of this InlineResponse2007.  # noqa: E501
        :rtype: ResponseMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this InlineResponse2007.


        :param meta: The meta of this InlineResponse2007.  # noqa: E501
        :type: ResponseMeta
        """

        self._meta = meta

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
        if issubclass(InlineResponse2007, dict):
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
        if not isinstance(other, InlineResponse2007):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
