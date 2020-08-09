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


class NewEvaluation(object):
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
        'time_stamp': 'datetime',
        'initial': 'str',
        'appetite_dry': 'float',
        'appetite_wet': 'float',
        'time': 'str',
        'drinking': 'float',
        'vomit': 'str',
        'cough': 'bool',
        'sneeze': 'bool',
        'urine': 'str',
        'stool': 'int',
        'animal': 'int',
        'enrichment_session': 'int',
        'elimination': 'bool',
        'shredded': 'bool',
        'digging': 'bool',
        'toys_chewed': 'bool',
        'water_flip': 'bool',
        'behavior_assessment': 'float',
        'weight': 'float'
    }

    attribute_map = {
        'id': 'id',
        'time_stamp': 'timeStamp',
        'initial': 'initial',
        'appetite_dry': 'appetiteDry',
        'appetite_wet': 'appetiteWet',
        'time': 'time',
        'drinking': 'drinking',
        'vomit': 'vomit',
        'cough': 'cough',
        'sneeze': 'sneeze',
        'urine': 'urine',
        'stool': 'stool',
        'animal': 'animal',
        'enrichment_session': 'enrichmentSession',
        'elimination': 'elimination',
        'shredded': 'shredded',
        'digging': 'digging',
        'toys_chewed': 'toys-chewed',
        'water_flip': 'water-flip',
        'behavior_assessment': 'behavior_assessment',
        'weight': 'weight'
    }

    def __init__(self, id=None, time_stamp=None, initial=None, appetite_dry=None, appetite_wet=None, time=None, drinking=None, vomit=None, cough=None, sneeze=None, urine=None, stool=None, animal=None, enrichment_session=None, elimination=None, shredded=None, digging=None, toys_chewed=None, water_flip=None, behavior_assessment=None, weight=None):  # noqa: E501
        """NewEvaluation - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._time_stamp = None
        self._initial = None
        self._appetite_dry = None
        self._appetite_wet = None
        self._time = None
        self._drinking = None
        self._vomit = None
        self._cough = None
        self._sneeze = None
        self._urine = None
        self._stool = None
        self._animal = None
        self._enrichment_session = None
        self._elimination = None
        self._shredded = None
        self._digging = None
        self._toys_chewed = None
        self._water_flip = None
        self._behavior_assessment = None
        self._weight = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if time_stamp is not None:
            self.time_stamp = time_stamp
        if initial is not None:
            self.initial = initial
        if appetite_dry is not None:
            self.appetite_dry = appetite_dry
        if appetite_wet is not None:
            self.appetite_wet = appetite_wet
        if time is not None:
            self.time = time
        if drinking is not None:
            self.drinking = drinking
        if vomit is not None:
            self.vomit = vomit
        if cough is not None:
            self.cough = cough
        if sneeze is not None:
            self.sneeze = sneeze
        if urine is not None:
            self.urine = urine
        if stool is not None:
            self.stool = stool
        if animal is not None:
            self.animal = animal
        if enrichment_session is not None:
            self.enrichment_session = enrichment_session
        if elimination is not None:
            self.elimination = elimination
        if shredded is not None:
            self.shredded = shredded
        if digging is not None:
            self.digging = digging
        if toys_chewed is not None:
            self.toys_chewed = toys_chewed
        if water_flip is not None:
            self.water_flip = water_flip
        if behavior_assessment is not None:
            self.behavior_assessment = behavior_assessment
        if weight is not None:
            self.weight = weight

    @property
    def id(self):
        """Gets the id of this NewEvaluation.  # noqa: E501


        :return: The id of this NewEvaluation.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NewEvaluation.


        :param id: The id of this NewEvaluation.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def time_stamp(self):
        """Gets the time_stamp of this NewEvaluation.  # noqa: E501


        :return: The time_stamp of this NewEvaluation.  # noqa: E501
        :rtype: datetime
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this NewEvaluation.


        :param time_stamp: The time_stamp of this NewEvaluation.  # noqa: E501
        :type: datetime
        """

        self._time_stamp = time_stamp

    @property
    def initial(self):
        """Gets the initial of this NewEvaluation.  # noqa: E501


        :return: The initial of this NewEvaluation.  # noqa: E501
        :rtype: str
        """
        return self._initial

    @initial.setter
    def initial(self, initial):
        """Sets the initial of this NewEvaluation.


        :param initial: The initial of this NewEvaluation.  # noqa: E501
        :type: str
        """

        self._initial = initial

    @property
    def appetite_dry(self):
        """Gets the appetite_dry of this NewEvaluation.  # noqa: E501


        :return: The appetite_dry of this NewEvaluation.  # noqa: E501
        :rtype: float
        """
        return self._appetite_dry

    @appetite_dry.setter
    def appetite_dry(self, appetite_dry):
        """Sets the appetite_dry of this NewEvaluation.


        :param appetite_dry: The appetite_dry of this NewEvaluation.  # noqa: E501
        :type: float
        """

        self._appetite_dry = appetite_dry

    @property
    def appetite_wet(self):
        """Gets the appetite_wet of this NewEvaluation.  # noqa: E501


        :return: The appetite_wet of this NewEvaluation.  # noqa: E501
        :rtype: float
        """
        return self._appetite_wet

    @appetite_wet.setter
    def appetite_wet(self, appetite_wet):
        """Sets the appetite_wet of this NewEvaluation.


        :param appetite_wet: The appetite_wet of this NewEvaluation.  # noqa: E501
        :type: float
        """

        self._appetite_wet = appetite_wet

    @property
    def time(self):
        """Gets the time of this NewEvaluation.  # noqa: E501


        :return: The time of this NewEvaluation.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this NewEvaluation.


        :param time: The time of this NewEvaluation.  # noqa: E501
        :type: str
        """

        self._time = time

    @property
    def drinking(self):
        """Gets the drinking of this NewEvaluation.  # noqa: E501


        :return: The drinking of this NewEvaluation.  # noqa: E501
        :rtype: float
        """
        return self._drinking

    @drinking.setter
    def drinking(self, drinking):
        """Sets the drinking of this NewEvaluation.


        :param drinking: The drinking of this NewEvaluation.  # noqa: E501
        :type: float
        """

        self._drinking = drinking

    @property
    def vomit(self):
        """Gets the vomit of this NewEvaluation.  # noqa: E501


        :return: The vomit of this NewEvaluation.  # noqa: E501
        :rtype: str
        """
        return self._vomit

    @vomit.setter
    def vomit(self, vomit):
        """Sets the vomit of this NewEvaluation.


        :param vomit: The vomit of this NewEvaluation.  # noqa: E501
        :type: str
        """

        self._vomit = vomit

    @property
    def cough(self):
        """Gets the cough of this NewEvaluation.  # noqa: E501


        :return: The cough of this NewEvaluation.  # noqa: E501
        :rtype: bool
        """
        return self._cough

    @cough.setter
    def cough(self, cough):
        """Sets the cough of this NewEvaluation.


        :param cough: The cough of this NewEvaluation.  # noqa: E501
        :type: bool
        """

        self._cough = cough

    @property
    def sneeze(self):
        """Gets the sneeze of this NewEvaluation.  # noqa: E501


        :return: The sneeze of this NewEvaluation.  # noqa: E501
        :rtype: bool
        """
        return self._sneeze

    @sneeze.setter
    def sneeze(self, sneeze):
        """Sets the sneeze of this NewEvaluation.


        :param sneeze: The sneeze of this NewEvaluation.  # noqa: E501
        :type: bool
        """

        self._sneeze = sneeze

    @property
    def urine(self):
        """Gets the urine of this NewEvaluation.  # noqa: E501


        :return: The urine of this NewEvaluation.  # noqa: E501
        :rtype: str
        """
        return self._urine

    @urine.setter
    def urine(self, urine):
        """Sets the urine of this NewEvaluation.


        :param urine: The urine of this NewEvaluation.  # noqa: E501
        :type: str
        """

        self._urine = urine

    @property
    def stool(self):
        """Gets the stool of this NewEvaluation.  # noqa: E501


        :return: The stool of this NewEvaluation.  # noqa: E501
        :rtype: int
        """
        return self._stool

    @stool.setter
    def stool(self, stool):
        """Sets the stool of this NewEvaluation.


        :param stool: The stool of this NewEvaluation.  # noqa: E501
        :type: int
        """

        self._stool = stool

    @property
    def animal(self):
        """Gets the animal of this NewEvaluation.  # noqa: E501


        :return: The animal of this NewEvaluation.  # noqa: E501
        :rtype: int
        """
        return self._animal

    @animal.setter
    def animal(self, animal):
        """Sets the animal of this NewEvaluation.


        :param animal: The animal of this NewEvaluation.  # noqa: E501
        :type: int
        """

        self._animal = animal

    @property
    def enrichment_session(self):
        """Gets the enrichment_session of this NewEvaluation.  # noqa: E501


        :return: The enrichment_session of this NewEvaluation.  # noqa: E501
        :rtype: int
        """
        return self._enrichment_session

    @enrichment_session.setter
    def enrichment_session(self, enrichment_session):
        """Sets the enrichment_session of this NewEvaluation.


        :param enrichment_session: The enrichment_session of this NewEvaluation.  # noqa: E501
        :type: int
        """

        self._enrichment_session = enrichment_session

    @property
    def elimination(self):
        """Gets the elimination of this NewEvaluation.  # noqa: E501


        :return: The elimination of this NewEvaluation.  # noqa: E501
        :rtype: bool
        """
        return self._elimination

    @elimination.setter
    def elimination(self, elimination):
        """Sets the elimination of this NewEvaluation.


        :param elimination: The elimination of this NewEvaluation.  # noqa: E501
        :type: bool
        """

        self._elimination = elimination

    @property
    def shredded(self):
        """Gets the shredded of this NewEvaluation.  # noqa: E501


        :return: The shredded of this NewEvaluation.  # noqa: E501
        :rtype: bool
        """
        return self._shredded

    @shredded.setter
    def shredded(self, shredded):
        """Sets the shredded of this NewEvaluation.


        :param shredded: The shredded of this NewEvaluation.  # noqa: E501
        :type: bool
        """

        self._shredded = shredded

    @property
    def digging(self):
        """Gets the digging of this NewEvaluation.  # noqa: E501


        :return: The digging of this NewEvaluation.  # noqa: E501
        :rtype: bool
        """
        return self._digging

    @digging.setter
    def digging(self, digging):
        """Sets the digging of this NewEvaluation.


        :param digging: The digging of this NewEvaluation.  # noqa: E501
        :type: bool
        """

        self._digging = digging

    @property
    def toys_chewed(self):
        """Gets the toys_chewed of this NewEvaluation.  # noqa: E501


        :return: The toys_chewed of this NewEvaluation.  # noqa: E501
        :rtype: bool
        """
        return self._toys_chewed

    @toys_chewed.setter
    def toys_chewed(self, toys_chewed):
        """Sets the toys_chewed of this NewEvaluation.


        :param toys_chewed: The toys_chewed of this NewEvaluation.  # noqa: E501
        :type: bool
        """

        self._toys_chewed = toys_chewed

    @property
    def water_flip(self):
        """Gets the water_flip of this NewEvaluation.  # noqa: E501


        :return: The water_flip of this NewEvaluation.  # noqa: E501
        :rtype: bool
        """
        return self._water_flip

    @water_flip.setter
    def water_flip(self, water_flip):
        """Sets the water_flip of this NewEvaluation.


        :param water_flip: The water_flip of this NewEvaluation.  # noqa: E501
        :type: bool
        """

        self._water_flip = water_flip

    @property
    def behavior_assessment(self):
        """Gets the behavior_assessment of this NewEvaluation.  # noqa: E501


        :return: The behavior_assessment of this NewEvaluation.  # noqa: E501
        :rtype: float
        """
        return self._behavior_assessment

    @behavior_assessment.setter
    def behavior_assessment(self, behavior_assessment):
        """Sets the behavior_assessment of this NewEvaluation.


        :param behavior_assessment: The behavior_assessment of this NewEvaluation.  # noqa: E501
        :type: float
        """

        self._behavior_assessment = behavior_assessment

    @property
    def weight(self):
        """Gets the weight of this NewEvaluation.  # noqa: E501


        :return: The weight of this NewEvaluation.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this NewEvaluation.


        :param weight: The weight of this NewEvaluation.  # noqa: E501
        :type: float
        """

        self._weight = weight

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
        if issubclass(NewEvaluation, dict):
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
        if not isinstance(other, NewEvaluation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
