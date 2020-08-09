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

class InlineResponse20037Dates(object):
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
        '_date': 'date',
        'total': 'float'
    }

    attribute_map = {
        '_date': 'date',
        'total': 'total'
    }

    def __init__(self, _date=None, total=None):  # noqa: E501
        """InlineResponse20037Dates - a model defined in Swagger"""  # noqa: E501
        self.__date = None
        self._total = None
        self.discriminator = None
        if _date is not None:
            self._date = _date
        if total is not None:
            self.total = total

    @property
    def _date(self):
        """Gets the _date of this InlineResponse20037Dates.  # noqa: E501


        :return: The _date of this InlineResponse20037Dates.  # noqa: E501
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this InlineResponse20037Dates.


        :param _date: The _date of this InlineResponse20037Dates.  # noqa: E501
        :type: date
        """

        self.__date = _date

    @property
    def total(self):
        """Gets the total of this InlineResponse20037Dates.  # noqa: E501


        :return: The total of this InlineResponse20037Dates.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this InlineResponse20037Dates.


        :param total: The total of this InlineResponse20037Dates.  # noqa: E501
        :type: float
        """

        self._total = total

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
        if issubclass(InlineResponse20037Dates, dict):
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
        if not isinstance(other, InlineResponse20037Dates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
