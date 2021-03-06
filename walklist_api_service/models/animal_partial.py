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


class AnimalPartial(object):
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
        'a_number': 'int',
        'name': 'str',
        'active': 'bool',
        'origin': 'str',
        'breed': 'str',
        'has_training_plan': 'bool',
        'note': 'str',
        'next_assessment_due': 'datetime',
        'arrival': 'datetime',
        'created': 'datetime',
        'animal_type': 'int',
        'location': 'int',
        'colour_code': 'int',
        'assessments': 'list[int]',
        'special_needs': 'list[int]'
    }

    attribute_map = {
        'a_number': 'aNumber',
        'name': 'name',
        'active': 'active',
        'origin': 'origin',
        'breed': 'breed',
        'has_training_plan': 'hasTrainingPlan',
        'note': 'note',
        'next_assessment_due': 'nextAssessmentDue',
        'arrival': 'arrival',
        'created': 'created',
        'animal_type': 'animalType',
        'location': 'location',
        'colour_code': 'colourCode',
        'assessments': 'assessments',
        'special_needs': 'specialNeeds'
    }

    def __init__(self, a_number=None, name=None, active=None, origin=None, breed=None, has_training_plan=None, note=None, next_assessment_due=None, arrival=None, created=None, animal_type=None, location=None, colour_code=None, assessments=None, special_needs=None):  # noqa: E501
        """AnimalPartial - a model defined in Swagger"""  # noqa: E501
        self._a_number = None
        self._name = None
        self._active = None
        self._origin = None
        self._breed = None
        self._has_training_plan = None
        self._note = None
        self._next_assessment_due = None
        self._arrival = None
        self._created = None
        self._animal_type = None
        self._location = None
        self._colour_code = None
        self._assessments = None
        self._special_needs = None
        self.discriminator = None
        if a_number is not None:
            self.a_number = a_number
        if name is not None:
            self.name = name
        if active is not None:
            self.active = active
        if origin is not None:
            self.origin = origin
        if breed is not None:
            self.breed = breed
        if has_training_plan is not None:
            self.has_training_plan = has_training_plan
        if note is not None:
            self.note = note
        if next_assessment_due is not None:
            self.next_assessment_due = next_assessment_due
        if arrival is not None:
            self.arrival = arrival
        if created is not None:
            self.created = created
        if animal_type is not None:
            self.animal_type = animal_type
        if location is not None:
            self.location = location
        if colour_code is not None:
            self.colour_code = colour_code
        if assessments is not None:
            self.assessments = assessments
        if special_needs is not None:
            self.special_needs = special_needs

    @property
    def a_number(self):
        """Gets the a_number of this AnimalPartial.  # noqa: E501


        :return: The a_number of this AnimalPartial.  # noqa: E501
        :rtype: int
        """
        return self._a_number

    @a_number.setter
    def a_number(self, a_number):
        """Sets the a_number of this AnimalPartial.


        :param a_number: The a_number of this AnimalPartial.  # noqa: E501
        :type: int
        """

        self._a_number = a_number

    @property
    def name(self):
        """Gets the name of this AnimalPartial.  # noqa: E501


        :return: The name of this AnimalPartial.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AnimalPartial.


        :param name: The name of this AnimalPartial.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def active(self):
        """Gets the active of this AnimalPartial.  # noqa: E501


        :return: The active of this AnimalPartial.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this AnimalPartial.


        :param active: The active of this AnimalPartial.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def origin(self):
        """Gets the origin of this AnimalPartial.  # noqa: E501


        :return: The origin of this AnimalPartial.  # noqa: E501
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this AnimalPartial.


        :param origin: The origin of this AnimalPartial.  # noqa: E501
        :type: str
        """

        self._origin = origin

    @property
    def breed(self):
        """Gets the breed of this AnimalPartial.  # noqa: E501


        :return: The breed of this AnimalPartial.  # noqa: E501
        :rtype: str
        """
        return self._breed

    @breed.setter
    def breed(self, breed):
        """Sets the breed of this AnimalPartial.


        :param breed: The breed of this AnimalPartial.  # noqa: E501
        :type: str
        """

        self._breed = breed

    @property
    def has_training_plan(self):
        """Gets the has_training_plan of this AnimalPartial.  # noqa: E501


        :return: The has_training_plan of this AnimalPartial.  # noqa: E501
        :rtype: bool
        """
        return self._has_training_plan

    @has_training_plan.setter
    def has_training_plan(self, has_training_plan):
        """Sets the has_training_plan of this AnimalPartial.


        :param has_training_plan: The has_training_plan of this AnimalPartial.  # noqa: E501
        :type: bool
        """

        self._has_training_plan = has_training_plan

    @property
    def note(self):
        """Gets the note of this AnimalPartial.  # noqa: E501


        :return: The note of this AnimalPartial.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this AnimalPartial.


        :param note: The note of this AnimalPartial.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def next_assessment_due(self):
        """Gets the next_assessment_due of this AnimalPartial.  # noqa: E501


        :return: The next_assessment_due of this AnimalPartial.  # noqa: E501
        :rtype: datetime
        """
        return self._next_assessment_due

    @next_assessment_due.setter
    def next_assessment_due(self, next_assessment_due):
        """Sets the next_assessment_due of this AnimalPartial.


        :param next_assessment_due: The next_assessment_due of this AnimalPartial.  # noqa: E501
        :type: datetime
        """

        self._next_assessment_due = next_assessment_due

    @property
    def arrival(self):
        """Gets the arrival of this AnimalPartial.  # noqa: E501


        :return: The arrival of this AnimalPartial.  # noqa: E501
        :rtype: datetime
        """
        return self._arrival

    @arrival.setter
    def arrival(self, arrival):
        """Sets the arrival of this AnimalPartial.


        :param arrival: The arrival of this AnimalPartial.  # noqa: E501
        :type: datetime
        """

        self._arrival = arrival

    @property
    def created(self):
        """Gets the created of this AnimalPartial.  # noqa: E501


        :return: The created of this AnimalPartial.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this AnimalPartial.


        :param created: The created of this AnimalPartial.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def animal_type(self):
        """Gets the animal_type of this AnimalPartial.  # noqa: E501


        :return: The animal_type of this AnimalPartial.  # noqa: E501
        :rtype: int
        """
        return self._animal_type

    @animal_type.setter
    def animal_type(self, animal_type):
        """Sets the animal_type of this AnimalPartial.


        :param animal_type: The animal_type of this AnimalPartial.  # noqa: E501
        :type: int
        """

        self._animal_type = animal_type

    @property
    def location(self):
        """Gets the location of this AnimalPartial.  # noqa: E501


        :return: The location of this AnimalPartial.  # noqa: E501
        :rtype: int
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this AnimalPartial.


        :param location: The location of this AnimalPartial.  # noqa: E501
        :type: int
        """

        self._location = location

    @property
    def colour_code(self):
        """Gets the colour_code of this AnimalPartial.  # noqa: E501


        :return: The colour_code of this AnimalPartial.  # noqa: E501
        :rtype: int
        """
        return self._colour_code

    @colour_code.setter
    def colour_code(self, colour_code):
        """Sets the colour_code of this AnimalPartial.


        :param colour_code: The colour_code of this AnimalPartial.  # noqa: E501
        :type: int
        """

        self._colour_code = colour_code

    @property
    def assessments(self):
        """Gets the assessments of this AnimalPartial.  # noqa: E501


        :return: The assessments of this AnimalPartial.  # noqa: E501
        :rtype: list[int]
        """
        return self._assessments

    @assessments.setter
    def assessments(self, assessments):
        """Sets the assessments of this AnimalPartial.


        :param assessments: The assessments of this AnimalPartial.  # noqa: E501
        :type: list[int]
        """

        self._assessments = assessments

    @property
    def special_needs(self):
        """Gets the special_needs of this AnimalPartial.  # noqa: E501


        :return: The special_needs of this AnimalPartial.  # noqa: E501
        :rtype: list[int]
        """
        return self._special_needs

    @special_needs.setter
    def special_needs(self, special_needs):
        """Sets the special_needs of this AnimalPartial.


        :param special_needs: The special_needs of this AnimalPartial.  # noqa: E501
        :type: list[int]
        """

        self._special_needs = special_needs

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
        if issubclass(AnimalPartial, dict):
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
        if not isinstance(other, AnimalPartial):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
