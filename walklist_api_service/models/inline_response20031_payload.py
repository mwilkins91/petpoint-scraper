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

class InlineResponse20031Payload(object):
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
        'enrichment_type': 'EnrichmentSessionPartial',
        'percent_of_total': 'float',
        'minutes': 'float'
    }

    attribute_map = {
        'enrichment_type': 'enrichment_type',
        'percent_of_total': 'percent_of_total',
        'minutes': 'minutes'
    }

    def __init__(self, enrichment_type=None, percent_of_total=None, minutes=None):  # noqa: E501
        """InlineResponse20031Payload - a model defined in Swagger"""  # noqa: E501
        self._enrichment_type = None
        self._percent_of_total = None
        self._minutes = None
        self.discriminator = None
        if enrichment_type is not None:
            self.enrichment_type = enrichment_type
        if percent_of_total is not None:
            self.percent_of_total = percent_of_total
        if minutes is not None:
            self.minutes = minutes

    @property
    def enrichment_type(self):
        """Gets the enrichment_type of this InlineResponse20031Payload.  # noqa: E501


        :return: The enrichment_type of this InlineResponse20031Payload.  # noqa: E501
        :rtype: EnrichmentSessionPartial
        """
        return self._enrichment_type

    @enrichment_type.setter
    def enrichment_type(self, enrichment_type):
        """Sets the enrichment_type of this InlineResponse20031Payload.


        :param enrichment_type: The enrichment_type of this InlineResponse20031Payload.  # noqa: E501
        :type: EnrichmentSessionPartial
        """

        self._enrichment_type = enrichment_type

    @property
    def percent_of_total(self):
        """Gets the percent_of_total of this InlineResponse20031Payload.  # noqa: E501


        :return: The percent_of_total of this InlineResponse20031Payload.  # noqa: E501
        :rtype: float
        """
        return self._percent_of_total

    @percent_of_total.setter
    def percent_of_total(self, percent_of_total):
        """Sets the percent_of_total of this InlineResponse20031Payload.


        :param percent_of_total: The percent_of_total of this InlineResponse20031Payload.  # noqa: E501
        :type: float
        """

        self._percent_of_total = percent_of_total

    @property
    def minutes(self):
        """Gets the minutes of this InlineResponse20031Payload.  # noqa: E501


        :return: The minutes of this InlineResponse20031Payload.  # noqa: E501
        :rtype: float
        """
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        """Sets the minutes of this InlineResponse20031Payload.


        :param minutes: The minutes of this InlineResponse20031Payload.  # noqa: E501
        :type: float
        """

        self._minutes = minutes

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
        if issubclass(InlineResponse20031Payload, dict):
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
        if not isinstance(other, InlineResponse20031Payload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
