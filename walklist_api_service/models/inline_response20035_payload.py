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

class InlineResponse20035Payload(object):
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
        'dates': 'list[InlineResponse20035PayloadDates]',
        'total_count_by_colour_code': 'object',
        'colour_codes': 'list[str]'
    }

    attribute_map = {
        'dates': 'dates',
        'total_count_by_colour_code': 'total_count_by_colour_code',
        'colour_codes': 'colour_codes'
    }

    def __init__(self, dates=None, total_count_by_colour_code=None, colour_codes=None):  # noqa: E501
        """InlineResponse20035Payload - a model defined in Swagger"""  # noqa: E501
        self._dates = None
        self._total_count_by_colour_code = None
        self._colour_codes = None
        self.discriminator = None
        if dates is not None:
            self.dates = dates
        if total_count_by_colour_code is not None:
            self.total_count_by_colour_code = total_count_by_colour_code
        if colour_codes is not None:
            self.colour_codes = colour_codes

    @property
    def dates(self):
        """Gets the dates of this InlineResponse20035Payload.  # noqa: E501


        :return: The dates of this InlineResponse20035Payload.  # noqa: E501
        :rtype: list[InlineResponse20035PayloadDates]
        """
        return self._dates

    @dates.setter
    def dates(self, dates):
        """Sets the dates of this InlineResponse20035Payload.


        :param dates: The dates of this InlineResponse20035Payload.  # noqa: E501
        :type: list[InlineResponse20035PayloadDates]
        """

        self._dates = dates

    @property
    def total_count_by_colour_code(self):
        """Gets the total_count_by_colour_code of this InlineResponse20035Payload.  # noqa: E501


        :return: The total_count_by_colour_code of this InlineResponse20035Payload.  # noqa: E501
        :rtype: object
        """
        return self._total_count_by_colour_code

    @total_count_by_colour_code.setter
    def total_count_by_colour_code(self, total_count_by_colour_code):
        """Sets the total_count_by_colour_code of this InlineResponse20035Payload.


        :param total_count_by_colour_code: The total_count_by_colour_code of this InlineResponse20035Payload.  # noqa: E501
        :type: object
        """

        self._total_count_by_colour_code = total_count_by_colour_code

    @property
    def colour_codes(self):
        """Gets the colour_codes of this InlineResponse20035Payload.  # noqa: E501


        :return: The colour_codes of this InlineResponse20035Payload.  # noqa: E501
        :rtype: list[str]
        """
        return self._colour_codes

    @colour_codes.setter
    def colour_codes(self, colour_codes):
        """Sets the colour_codes of this InlineResponse20035Payload.


        :param colour_codes: The colour_codes of this InlineResponse20035Payload.  # noqa: E501
        :type: list[str]
        """

        self._colour_codes = colour_codes

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
        if issubclass(InlineResponse20035Payload, dict):
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
        if not isinstance(other, InlineResponse20035Payload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other