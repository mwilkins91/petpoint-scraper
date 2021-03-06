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


class NewActiveEnrichmentSession(object):
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
        'depart': 'datetime',
        'walker_name': 'str',
        'human_type': 'int',
        'enrichment_type': 'str',
        'color_code_at_time_of_enrichment': 'str',
        'animal': 'int'
    }

    attribute_map = {
        'id': 'id',
        'depart': 'depart',
        'walker_name': 'walkerName',
        'human_type': 'humanType',
        'enrichment_type': 'enrichmentType',
        'color_code_at_time_of_enrichment': 'colorCodeAtTimeOfEnrichment',
        'animal': 'animal'
    }

    def __init__(self, id=None, depart=None, walker_name=None, human_type=None, enrichment_type=None, color_code_at_time_of_enrichment=None, animal=None):  # noqa: E501
        """NewActiveEnrichmentSession - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._depart = None
        self._walker_name = None
        self._human_type = None
        self._enrichment_type = None
        self._color_code_at_time_of_enrichment = None
        self._animal = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if depart is not None:
            self.depart = depart
        self.walker_name = walker_name
        self.human_type = human_type
        self.enrichment_type = enrichment_type
        self.color_code_at_time_of_enrichment = color_code_at_time_of_enrichment
        if animal is not None:
            self.animal = animal

    @property
    def id(self):
        """Gets the id of this NewActiveEnrichmentSession.  # noqa: E501


        :return: The id of this NewActiveEnrichmentSession.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NewActiveEnrichmentSession.


        :param id: The id of this NewActiveEnrichmentSession.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def depart(self):
        """Gets the depart of this NewActiveEnrichmentSession.  # noqa: E501


        :return: The depart of this NewActiveEnrichmentSession.  # noqa: E501
        :rtype: datetime
        """
        return self._depart

    @depart.setter
    def depart(self, depart):
        """Sets the depart of this NewActiveEnrichmentSession.


        :param depart: The depart of this NewActiveEnrichmentSession.  # noqa: E501
        :type: datetime
        """

        self._depart = depart

    @property
    def walker_name(self):
        """Gets the walker_name of this NewActiveEnrichmentSession.  # noqa: E501


        :return: The walker_name of this NewActiveEnrichmentSession.  # noqa: E501
        :rtype: str
        """
        return self._walker_name

    @walker_name.setter
    def walker_name(self, walker_name):
        """Sets the walker_name of this NewActiveEnrichmentSession.


        :param walker_name: The walker_name of this NewActiveEnrichmentSession.  # noqa: E501
        :type: str
        """
        if walker_name is None:
            raise ValueError("Invalid value for `walker_name`, must not be `None`")  # noqa: E501

        self._walker_name = walker_name

    @property
    def human_type(self):
        """Gets the human_type of this NewActiveEnrichmentSession.  # noqa: E501


        :return: The human_type of this NewActiveEnrichmentSession.  # noqa: E501
        :rtype: int
        """
        return self._human_type

    @human_type.setter
    def human_type(self, human_type):
        """Sets the human_type of this NewActiveEnrichmentSession.


        :param human_type: The human_type of this NewActiveEnrichmentSession.  # noqa: E501
        :type: int
        """
        if human_type is None:
            raise ValueError("Invalid value for `human_type`, must not be `None`")  # noqa: E501

        self._human_type = human_type

    @property
    def enrichment_type(self):
        """Gets the enrichment_type of this NewActiveEnrichmentSession.  # noqa: E501


        :return: The enrichment_type of this NewActiveEnrichmentSession.  # noqa: E501
        :rtype: str
        """
        return self._enrichment_type

    @enrichment_type.setter
    def enrichment_type(self, enrichment_type):
        """Sets the enrichment_type of this NewActiveEnrichmentSession.


        :param enrichment_type: The enrichment_type of this NewActiveEnrichmentSession.  # noqa: E501
        :type: str
        """
        if enrichment_type is None:
            raise ValueError("Invalid value for `enrichment_type`, must not be `None`")  # noqa: E501

        self._enrichment_type = enrichment_type

    @property
    def color_code_at_time_of_enrichment(self):
        """Gets the color_code_at_time_of_enrichment of this NewActiveEnrichmentSession.  # noqa: E501


        :return: The color_code_at_time_of_enrichment of this NewActiveEnrichmentSession.  # noqa: E501
        :rtype: str
        """
        return self._color_code_at_time_of_enrichment

    @color_code_at_time_of_enrichment.setter
    def color_code_at_time_of_enrichment(self, color_code_at_time_of_enrichment):
        """Sets the color_code_at_time_of_enrichment of this NewActiveEnrichmentSession.


        :param color_code_at_time_of_enrichment: The color_code_at_time_of_enrichment of this NewActiveEnrichmentSession.  # noqa: E501
        :type: str
        """
        if color_code_at_time_of_enrichment is None:
            raise ValueError("Invalid value for `color_code_at_time_of_enrichment`, must not be `None`")  # noqa: E501

        self._color_code_at_time_of_enrichment = color_code_at_time_of_enrichment

    @property
    def animal(self):
        """Gets the animal of this NewActiveEnrichmentSession.  # noqa: E501


        :return: The animal of this NewActiveEnrichmentSession.  # noqa: E501
        :rtype: int
        """
        return self._animal

    @animal.setter
    def animal(self, animal):
        """Sets the animal of this NewActiveEnrichmentSession.


        :param animal: The animal of this NewActiveEnrichmentSession.  # noqa: E501
        :type: int
        """

        self._animal = animal

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
        if issubclass(NewActiveEnrichmentSession, dict):
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
        if not isinstance(other, NewActiveEnrichmentSession):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
