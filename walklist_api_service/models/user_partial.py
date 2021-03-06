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


class UserPartial(object):
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
        'email': 'str',
        'password': 'str',
        'created': 'datetime',
        'access_level': 'int',
        'verified': 'bool',
        'is_update_expected': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'email': 'email',
        'password': 'password',
        'created': 'created',
        'access_level': 'accessLevel',
        'verified': 'verified',
        'is_update_expected': 'isUpdateExpected'
    }

    def __init__(self, id=None, name=None, email=None, password=None, created=None, access_level=None, verified=None, is_update_expected=None):  # noqa: E501
        """UserPartial - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._email = None
        self._password = None
        self._created = None
        self._access_level = None
        self._verified = None
        self._is_update_expected = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        if password is not None:
            self.password = password
        if created is not None:
            self.created = created
        if access_level is not None:
            self.access_level = access_level
        if verified is not None:
            self.verified = verified
        if is_update_expected is not None:
            self.is_update_expected = is_update_expected

    @property
    def id(self):
        """Gets the id of this UserPartial.  # noqa: E501


        :return: The id of this UserPartial.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserPartial.


        :param id: The id of this UserPartial.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this UserPartial.  # noqa: E501


        :return: The name of this UserPartial.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserPartial.


        :param name: The name of this UserPartial.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def email(self):
        """Gets the email of this UserPartial.  # noqa: E501


        :return: The email of this UserPartial.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserPartial.


        :param email: The email of this UserPartial.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def password(self):
        """Gets the password of this UserPartial.  # noqa: E501


        :return: The password of this UserPartial.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UserPartial.


        :param password: The password of this UserPartial.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def created(self):
        """Gets the created of this UserPartial.  # noqa: E501


        :return: The created of this UserPartial.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this UserPartial.


        :param created: The created of this UserPartial.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def access_level(self):
        """Gets the access_level of this UserPartial.  # noqa: E501


        :return: The access_level of this UserPartial.  # noqa: E501
        :rtype: int
        """
        return self._access_level

    @access_level.setter
    def access_level(self, access_level):
        """Sets the access_level of this UserPartial.


        :param access_level: The access_level of this UserPartial.  # noqa: E501
        :type: int
        """

        self._access_level = access_level

    @property
    def verified(self):
        """Gets the verified of this UserPartial.  # noqa: E501


        :return: The verified of this UserPartial.  # noqa: E501
        :rtype: bool
        """
        return self._verified

    @verified.setter
    def verified(self, verified):
        """Sets the verified of this UserPartial.


        :param verified: The verified of this UserPartial.  # noqa: E501
        :type: bool
        """

        self._verified = verified

    @property
    def is_update_expected(self):
        """Gets the is_update_expected of this UserPartial.  # noqa: E501


        :return: The is_update_expected of this UserPartial.  # noqa: E501
        :rtype: bool
        """
        return self._is_update_expected

    @is_update_expected.setter
    def is_update_expected(self, is_update_expected):
        """Sets the is_update_expected of this UserPartial.


        :param is_update_expected: The is_update_expected of this UserPartial.  # noqa: E501
        :type: bool
        """

        self._is_update_expected = is_update_expected

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
        if issubclass(UserPartial, dict):
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
        if not isinstance(other, UserPartial):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
