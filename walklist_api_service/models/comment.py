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


class Comment(object):
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
        'comment': 'str',
        'rating': 'int',
        'animal': 'Animal',
        'enrichment_session': 'EnrichmentSession'
    }

    attribute_map = {
        'id': 'id',
        'comment': 'comment',
        'rating': 'rating',
        'animal': 'animal',
        'enrichment_session': 'enrichmentSession'
    }

    def __init__(self, id=None, comment=None, rating=None, animal=None, enrichment_session=None):  # noqa: E501
        """Comment - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._comment = None
        self._rating = None
        self._animal = None
        self._enrichment_session = None
        self.discriminator = None
        self.id = id
        self.comment = comment
        self.rating = rating
        self.animal = animal
        self.enrichment_session = enrichment_session

    @property
    def id(self):
        """Gets the id of this Comment.  # noqa: E501


        :return: The id of this Comment.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Comment.


        :param id: The id of this Comment.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def comment(self):
        """Gets the comment of this Comment.  # noqa: E501


        :return: The comment of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Comment.


        :param comment: The comment of this Comment.  # noqa: E501
        :type: str
        """
        if comment is None:
            raise ValueError("Invalid value for `comment`, must not be `None`")  # noqa: E501

        self._comment = comment

    @property
    def rating(self):
        """Gets the rating of this Comment.  # noqa: E501


        :return: The rating of this Comment.  # noqa: E501
        :rtype: int
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this Comment.


        :param rating: The rating of this Comment.  # noqa: E501
        :type: int
        """
        if rating is None:
            raise ValueError("Invalid value for `rating`, must not be `None`")  # noqa: E501

        self._rating = rating

    @property
    def animal(self):
        """Gets the animal of this Comment.  # noqa: E501


        :return: The animal of this Comment.  # noqa: E501
        :rtype: Animal
        """
        return self._animal

    @animal.setter
    def animal(self, animal):
        """Sets the animal of this Comment.


        :param animal: The animal of this Comment.  # noqa: E501
        :type: Animal
        """
        if animal is None:
            raise ValueError("Invalid value for `animal`, must not be `None`")  # noqa: E501

        self._animal = animal

    @property
    def enrichment_session(self):
        """Gets the enrichment_session of this Comment.  # noqa: E501


        :return: The enrichment_session of this Comment.  # noqa: E501
        :rtype: EnrichmentSession
        """
        return self._enrichment_session

    @enrichment_session.setter
    def enrichment_session(self, enrichment_session):
        """Sets the enrichment_session of this Comment.


        :param enrichment_session: The enrichment_session of this Comment.  # noqa: E501
        :type: EnrichmentSession
        """
        if enrichment_session is None:
            raise ValueError("Invalid value for `enrichment_session`, must not be `None`")  # noqa: E501

        self._enrichment_session = enrichment_session

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
        if issubclass(Comment, dict):
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
        if not isinstance(other, Comment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
