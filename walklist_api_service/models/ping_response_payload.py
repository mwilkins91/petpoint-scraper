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


class PingResponsePayload(object):
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
        'greeting': 'str',
        '_date': 'str',
        'url': 'str',
        'headers': 'PingResponsePayloadHeaders'
    }

    attribute_map = {
        'greeting': 'greeting',
        '_date': 'date',
        'url': 'url',
        'headers': 'headers'
    }

    def __init__(self, greeting=None, _date=None, url=None, headers=None):  # noqa: E501
        """PingResponsePayload - a model defined in Swagger"""  # noqa: E501
        self._greeting = None
        self.__date = None
        self._url = None
        self._headers = None
        self.discriminator = None
        if greeting is not None:
            self.greeting = greeting
        if _date is not None:
            self._date = _date
        if url is not None:
            self.url = url
        if headers is not None:
            self.headers = headers

    @property
    def greeting(self):
        """Gets the greeting of this PingResponsePayload.  # noqa: E501


        :return: The greeting of this PingResponsePayload.  # noqa: E501
        :rtype: str
        """
        return self._greeting

    @greeting.setter
    def greeting(self, greeting):
        """Sets the greeting of this PingResponsePayload.


        :param greeting: The greeting of this PingResponsePayload.  # noqa: E501
        :type: str
        """

        self._greeting = greeting

    @property
    def _date(self):
        """Gets the _date of this PingResponsePayload.  # noqa: E501


        :return: The _date of this PingResponsePayload.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this PingResponsePayload.


        :param _date: The _date of this PingResponsePayload.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def url(self):
        """Gets the url of this PingResponsePayload.  # noqa: E501


        :return: The url of this PingResponsePayload.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PingResponsePayload.


        :param url: The url of this PingResponsePayload.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def headers(self):
        """Gets the headers of this PingResponsePayload.  # noqa: E501


        :return: The headers of this PingResponsePayload.  # noqa: E501
        :rtype: PingResponsePayloadHeaders
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this PingResponsePayload.


        :param headers: The headers of this PingResponsePayload.  # noqa: E501
        :type: PingResponsePayloadHeaders
        """

        self._headers = headers

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
        if issubclass(PingResponsePayload, dict):
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
        if not isinstance(other, PingResponsePayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
