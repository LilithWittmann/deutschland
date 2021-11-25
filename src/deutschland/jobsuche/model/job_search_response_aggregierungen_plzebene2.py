"""
    Bundesagentur für Arbeit: Jobsuche API

    Die größte Stellendatenbank Deutschlands durchsuchen, Details zu Stellenanzeigen und Informationen über Arbeitgeber abrufen. <br><br> Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs. Folgende Client-Credentials können dafür verwendet werden:<br><br> **ClientID:** c003a37f-024f-462a-b36d-b001be4cd24a <br> **ClientSecret:** 32a39620-32b3-4307-9aa1-511e3d7f48a8  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from deutschland.jobsuche.exceptions import ApiAttributeError
from deutschland.jobsuche.model_utils import ApiTypeError  # noqa: F401
from deutschland.jobsuche.model_utils import (
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

from ..model_utils import OpenApiModel


class JobSearchResponseAggregierungenPlzebene2(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {}

    validations = {}

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (
            bool,
            date,
            datetime,
            dict,
            float,
            int,
            list,
            str,
            none_type,
        )  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            "_10": (int,),  # noqa: E501
            "_12": (int,),  # noqa: E501
            "_13": (int,),  # noqa: E501
            "_14": (int,),  # noqa: E501
            "_15": (int,),  # noqa: E501
            "_16": (int,),  # noqa: E501
            "_17": (int,),  # noqa: E501
            "_18": (int,),  # noqa: E501
            "_19": (int,),  # noqa: E501
            "_20": (int,),  # noqa: E501
            "_21": (int,),  # noqa: E501
            "_22": (int,),  # noqa: E501
            "_23": (int,),  # noqa: E501
            "_24": (int,),  # noqa: E501
            "_25": (int,),  # noqa: E501
            "_26": (int,),  # noqa: E501
            "_27": (int,),  # noqa: E501
            "_28": (int,),  # noqa: E501
            "_29": (int,),  # noqa: E501
            "_30": (int,),  # noqa: E501
            "_31": (int,),  # noqa: E501
            "_32": (int,),  # noqa: E501
            "_33": (int,),  # noqa: E501
            "_34": (int,),  # noqa: E501
            "_35": (int,),  # noqa: E501
            "_36": (int,),  # noqa: E501
            "_37": (int,),  # noqa: E501
            "_38": (int,),  # noqa: E501
            "_39": (int,),  # noqa: E501
            "_40": (int,),  # noqa: E501
            "_41": (int,),  # noqa: E501
            "_42": (int,),  # noqa: E501
            "_44": (int,),  # noqa: E501
            "_45": (int,),  # noqa: E501
            "_46": (int,),  # noqa: E501
            "_47": (int,),  # noqa: E501
            "_48": (int,),  # noqa: E501
            "_49": (int,),  # noqa: E501
            "_50": (int,),  # noqa: E501
            "_51": (int,),  # noqa: E501
            "_52": (int,),  # noqa: E501
            "_53": (int,),  # noqa: E501
            "_54": (int,),  # noqa: E501
            "_55": (int,),  # noqa: E501
            "_56": (int,),  # noqa: E501
            "_57": (int,),  # noqa: E501
            "_58": (int,),  # noqa: E501
            "_59": (int,),  # noqa: E501
            "_60": (int,),  # noqa: E501
            "_61": (int,),  # noqa: E501
            "_63": (int,),  # noqa: E501
            "_64": (int,),  # noqa: E501
            "_65": (int,),  # noqa: E501
            "_66": (int,),  # noqa: E501
            "_67": (int,),  # noqa: E501
            "_68": (int,),  # noqa: E501
            "_69": (int,),  # noqa: E501
            "_70": (int,),  # noqa: E501
            "_71": (int,),  # noqa: E501
            "_72": (int,),  # noqa: E501
            "_73": (int,),  # noqa: E501
            "_74": (int,),  # noqa: E501
            "_75": (int,),  # noqa: E501
            "_76": (int,),  # noqa: E501
            "_77": (int,),  # noqa: E501
            "_78": (int,),  # noqa: E501
            "_79": (int,),  # noqa: E501
            "_80": (int,),  # noqa: E501
            "_81": (int,),  # noqa: E501
            "_82": (int,),  # noqa: E501
            "_83": (int,),  # noqa: E501
            "_84": (int,),  # noqa: E501
            "_85": (int,),  # noqa: E501
            "_86": (int,),  # noqa: E501
            "_87": (int,),  # noqa: E501
            "_88": (int,),  # noqa: E501
            "_89": (int,),  # noqa: E501
            "_90": (int,),  # noqa: E501
            "_91": (int,),  # noqa: E501
            "_92": (int,),  # noqa: E501
            "_93": (int,),  # noqa: E501
            "_94": (int,),  # noqa: E501
            "_95": (int,),  # noqa: E501
            "_96": (int,),  # noqa: E501
            "_97": (int,),  # noqa: E501
            "_98": (int,),  # noqa: E501
            "_99": (int,),  # noqa: E501
            "_01": (int,),  # noqa: E501
            "_02": (int,),  # noqa: E501
            "_03": (int,),  # noqa: E501
            "_04": (int,),  # noqa: E501
            "_06": (int,),  # noqa: E501
            "_07": (int,),  # noqa: E501
            "_08": (int,),  # noqa: E501
            "_09": (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        "_10": "10",  # noqa: E501
        "_12": "12",  # noqa: E501
        "_13": "13",  # noqa: E501
        "_14": "14",  # noqa: E501
        "_15": "15",  # noqa: E501
        "_16": "16",  # noqa: E501
        "_17": "17",  # noqa: E501
        "_18": "18",  # noqa: E501
        "_19": "19",  # noqa: E501
        "_20": "20",  # noqa: E501
        "_21": "21",  # noqa: E501
        "_22": "22",  # noqa: E501
        "_23": "23",  # noqa: E501
        "_24": "24",  # noqa: E501
        "_25": "25",  # noqa: E501
        "_26": "26",  # noqa: E501
        "_27": "27",  # noqa: E501
        "_28": "28",  # noqa: E501
        "_29": "29",  # noqa: E501
        "_30": "30",  # noqa: E501
        "_31": "31",  # noqa: E501
        "_32": "32",  # noqa: E501
        "_33": "33",  # noqa: E501
        "_34": "34",  # noqa: E501
        "_35": "35",  # noqa: E501
        "_36": "36",  # noqa: E501
        "_37": "37",  # noqa: E501
        "_38": "38",  # noqa: E501
        "_39": "39",  # noqa: E501
        "_40": "40",  # noqa: E501
        "_41": "41",  # noqa: E501
        "_42": "42",  # noqa: E501
        "_44": "44",  # noqa: E501
        "_45": "45",  # noqa: E501
        "_46": "46",  # noqa: E501
        "_47": "47",  # noqa: E501
        "_48": "48",  # noqa: E501
        "_49": "49",  # noqa: E501
        "_50": "50",  # noqa: E501
        "_51": "51",  # noqa: E501
        "_52": "52",  # noqa: E501
        "_53": "53",  # noqa: E501
        "_54": "54",  # noqa: E501
        "_55": "55",  # noqa: E501
        "_56": "56",  # noqa: E501
        "_57": "57",  # noqa: E501
        "_58": "58",  # noqa: E501
        "_59": "59",  # noqa: E501
        "_60": "60",  # noqa: E501
        "_61": "61",  # noqa: E501
        "_63": "63",  # noqa: E501
        "_64": "64",  # noqa: E501
        "_65": "65",  # noqa: E501
        "_66": "66",  # noqa: E501
        "_67": "67",  # noqa: E501
        "_68": "68",  # noqa: E501
        "_69": "69",  # noqa: E501
        "_70": "70",  # noqa: E501
        "_71": "71",  # noqa: E501
        "_72": "72",  # noqa: E501
        "_73": "73",  # noqa: E501
        "_74": "74",  # noqa: E501
        "_75": "75",  # noqa: E501
        "_76": "76",  # noqa: E501
        "_77": "77",  # noqa: E501
        "_78": "78",  # noqa: E501
        "_79": "79",  # noqa: E501
        "_80": "80",  # noqa: E501
        "_81": "81",  # noqa: E501
        "_82": "82",  # noqa: E501
        "_83": "83",  # noqa: E501
        "_84": "84",  # noqa: E501
        "_85": "85",  # noqa: E501
        "_86": "86",  # noqa: E501
        "_87": "87",  # noqa: E501
        "_88": "88",  # noqa: E501
        "_89": "89",  # noqa: E501
        "_90": "90",  # noqa: E501
        "_91": "91",  # noqa: E501
        "_92": "92",  # noqa: E501
        "_93": "93",  # noqa: E501
        "_94": "94",  # noqa: E501
        "_95": "95",  # noqa: E501
        "_96": "96",  # noqa: E501
        "_97": "97",  # noqa: E501
        "_98": "98",  # noqa: E501
        "_99": "99",  # noqa: E501
        "_01": "01",  # noqa: E501
        "_02": "02",  # noqa: E501
        "_03": "03",  # noqa: E501
        "_04": "04",  # noqa: E501
        "_06": "06",  # noqa: E501
        "_07": "07",  # noqa: E501
        "_08": "08",  # noqa: E501
        "_09": "09",  # noqa: E501
    }

    read_only_vars = {}

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """JobSearchResponseAggregierungenPlzebene2 - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            _10 (int): [optional]  # noqa: E501
            _12 (int): [optional]  # noqa: E501
            _13 (int): [optional]  # noqa: E501
            _14 (int): [optional]  # noqa: E501
            _15 (int): [optional]  # noqa: E501
            _16 (int): [optional]  # noqa: E501
            _17 (int): [optional]  # noqa: E501
            _18 (int): [optional]  # noqa: E501
            _19 (int): [optional]  # noqa: E501
            _20 (int): [optional]  # noqa: E501
            _21 (int): [optional]  # noqa: E501
            _22 (int): [optional]  # noqa: E501
            _23 (int): [optional]  # noqa: E501
            _24 (int): [optional]  # noqa: E501
            _25 (int): [optional]  # noqa: E501
            _26 (int): [optional]  # noqa: E501
            _27 (int): [optional]  # noqa: E501
            _28 (int): [optional]  # noqa: E501
            _29 (int): [optional]  # noqa: E501
            _30 (int): [optional]  # noqa: E501
            _31 (int): [optional]  # noqa: E501
            _32 (int): [optional]  # noqa: E501
            _33 (int): [optional]  # noqa: E501
            _34 (int): [optional]  # noqa: E501
            _35 (int): [optional]  # noqa: E501
            _36 (int): [optional]  # noqa: E501
            _37 (int): [optional]  # noqa: E501
            _38 (int): [optional]  # noqa: E501
            _39 (int): [optional]  # noqa: E501
            _40 (int): [optional]  # noqa: E501
            _41 (int): [optional]  # noqa: E501
            _42 (int): [optional]  # noqa: E501
            _44 (int): [optional]  # noqa: E501
            _45 (int): [optional]  # noqa: E501
            _46 (int): [optional]  # noqa: E501
            _47 (int): [optional]  # noqa: E501
            _48 (int): [optional]  # noqa: E501
            _49 (int): [optional]  # noqa: E501
            _50 (int): [optional]  # noqa: E501
            _51 (int): [optional]  # noqa: E501
            _52 (int): [optional]  # noqa: E501
            _53 (int): [optional]  # noqa: E501
            _54 (int): [optional]  # noqa: E501
            _55 (int): [optional]  # noqa: E501
            _56 (int): [optional]  # noqa: E501
            _57 (int): [optional]  # noqa: E501
            _58 (int): [optional]  # noqa: E501
            _59 (int): [optional]  # noqa: E501
            _60 (int): [optional]  # noqa: E501
            _61 (int): [optional]  # noqa: E501
            _63 (int): [optional]  # noqa: E501
            _64 (int): [optional]  # noqa: E501
            _65 (int): [optional]  # noqa: E501
            _66 (int): [optional]  # noqa: E501
            _67 (int): [optional]  # noqa: E501
            _68 (int): [optional]  # noqa: E501
            _69 (int): [optional]  # noqa: E501
            _70 (int): [optional]  # noqa: E501
            _71 (int): [optional]  # noqa: E501
            _72 (int): [optional]  # noqa: E501
            _73 (int): [optional]  # noqa: E501
            _74 (int): [optional]  # noqa: E501
            _75 (int): [optional]  # noqa: E501
            _76 (int): [optional]  # noqa: E501
            _77 (int): [optional]  # noqa: E501
            _78 (int): [optional]  # noqa: E501
            _79 (int): [optional]  # noqa: E501
            _80 (int): [optional]  # noqa: E501
            _81 (int): [optional]  # noqa: E501
            _82 (int): [optional]  # noqa: E501
            _83 (int): [optional]  # noqa: E501
            _84 (int): [optional]  # noqa: E501
            _85 (int): [optional]  # noqa: E501
            _86 (int): [optional]  # noqa: E501
            _87 (int): [optional]  # noqa: E501
            _88 (int): [optional]  # noqa: E501
            _89 (int): [optional]  # noqa: E501
            _90 (int): [optional]  # noqa: E501
            _91 (int): [optional]  # noqa: E501
            _92 (int): [optional]  # noqa: E501
            _93 (int): [optional]  # noqa: E501
            _94 (int): [optional]  # noqa: E501
            _95 (int): [optional]  # noqa: E501
            _96 (int): [optional]  # noqa: E501
            _97 (int): [optional]  # noqa: E501
            _98 (int): [optional]  # noqa: E501
            _99 (int): [optional]  # noqa: E501
            _01 (int): [optional]  # noqa: E501
            _02 (int): [optional]  # noqa: E501
            _03 (int): [optional]  # noqa: E501
            _04 (int): [optional]  # noqa: E501
            _06 (int): [optional]  # noqa: E501
            _07 (int): [optional]  # noqa: E501
            _08 (int): [optional]  # noqa: E501
            _09 (int): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set(
        [
            "_data_store",
            "_check_type",
            "_spec_property_naming",
            "_path_to_item",
            "_configuration",
            "_visited_composed_classes",
        ]
    )

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """JobSearchResponseAggregierungenPlzebene2 - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            _10 (int): [optional]  # noqa: E501
            _12 (int): [optional]  # noqa: E501
            _13 (int): [optional]  # noqa: E501
            _14 (int): [optional]  # noqa: E501
            _15 (int): [optional]  # noqa: E501
            _16 (int): [optional]  # noqa: E501
            _17 (int): [optional]  # noqa: E501
            _18 (int): [optional]  # noqa: E501
            _19 (int): [optional]  # noqa: E501
            _20 (int): [optional]  # noqa: E501
            _21 (int): [optional]  # noqa: E501
            _22 (int): [optional]  # noqa: E501
            _23 (int): [optional]  # noqa: E501
            _24 (int): [optional]  # noqa: E501
            _25 (int): [optional]  # noqa: E501
            _26 (int): [optional]  # noqa: E501
            _27 (int): [optional]  # noqa: E501
            _28 (int): [optional]  # noqa: E501
            _29 (int): [optional]  # noqa: E501
            _30 (int): [optional]  # noqa: E501
            _31 (int): [optional]  # noqa: E501
            _32 (int): [optional]  # noqa: E501
            _33 (int): [optional]  # noqa: E501
            _34 (int): [optional]  # noqa: E501
            _35 (int): [optional]  # noqa: E501
            _36 (int): [optional]  # noqa: E501
            _37 (int): [optional]  # noqa: E501
            _38 (int): [optional]  # noqa: E501
            _39 (int): [optional]  # noqa: E501
            _40 (int): [optional]  # noqa: E501
            _41 (int): [optional]  # noqa: E501
            _42 (int): [optional]  # noqa: E501
            _44 (int): [optional]  # noqa: E501
            _45 (int): [optional]  # noqa: E501
            _46 (int): [optional]  # noqa: E501
            _47 (int): [optional]  # noqa: E501
            _48 (int): [optional]  # noqa: E501
            _49 (int): [optional]  # noqa: E501
            _50 (int): [optional]  # noqa: E501
            _51 (int): [optional]  # noqa: E501
            _52 (int): [optional]  # noqa: E501
            _53 (int): [optional]  # noqa: E501
            _54 (int): [optional]  # noqa: E501
            _55 (int): [optional]  # noqa: E501
            _56 (int): [optional]  # noqa: E501
            _57 (int): [optional]  # noqa: E501
            _58 (int): [optional]  # noqa: E501
            _59 (int): [optional]  # noqa: E501
            _60 (int): [optional]  # noqa: E501
            _61 (int): [optional]  # noqa: E501
            _63 (int): [optional]  # noqa: E501
            _64 (int): [optional]  # noqa: E501
            _65 (int): [optional]  # noqa: E501
            _66 (int): [optional]  # noqa: E501
            _67 (int): [optional]  # noqa: E501
            _68 (int): [optional]  # noqa: E501
            _69 (int): [optional]  # noqa: E501
            _70 (int): [optional]  # noqa: E501
            _71 (int): [optional]  # noqa: E501
            _72 (int): [optional]  # noqa: E501
            _73 (int): [optional]  # noqa: E501
            _74 (int): [optional]  # noqa: E501
            _75 (int): [optional]  # noqa: E501
            _76 (int): [optional]  # noqa: E501
            _77 (int): [optional]  # noqa: E501
            _78 (int): [optional]  # noqa: E501
            _79 (int): [optional]  # noqa: E501
            _80 (int): [optional]  # noqa: E501
            _81 (int): [optional]  # noqa: E501
            _82 (int): [optional]  # noqa: E501
            _83 (int): [optional]  # noqa: E501
            _84 (int): [optional]  # noqa: E501
            _85 (int): [optional]  # noqa: E501
            _86 (int): [optional]  # noqa: E501
            _87 (int): [optional]  # noqa: E501
            _88 (int): [optional]  # noqa: E501
            _89 (int): [optional]  # noqa: E501
            _90 (int): [optional]  # noqa: E501
            _91 (int): [optional]  # noqa: E501
            _92 (int): [optional]  # noqa: E501
            _93 (int): [optional]  # noqa: E501
            _94 (int): [optional]  # noqa: E501
            _95 (int): [optional]  # noqa: E501
            _96 (int): [optional]  # noqa: E501
            _97 (int): [optional]  # noqa: E501
            _98 (int): [optional]  # noqa: E501
            _99 (int): [optional]  # noqa: E501
            _01 (int): [optional]  # noqa: E501
            _02 (int): [optional]  # noqa: E501
            _03 (int): [optional]  # noqa: E501
            _04 (int): [optional]  # noqa: E501
            _06 (int): [optional]  # noqa: E501
            _07 (int): [optional]  # noqa: E501
            _08 (int): [optional]  # noqa: E501
            _09 (int): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(
                    f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                    f"class with read only attributes."
                )
