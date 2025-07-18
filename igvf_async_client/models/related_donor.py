# coding: utf-8

"""
    IGVF Project API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 86.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class RelatedDonor(BaseModel):
    """
    Familial relation of this donor.
    """ # noqa: E501
    donor: StrictStr = Field(description="An identifier for the related donor.")
    relationship_type: StrictStr = Field(description="A descriptive term for the related donor’s relationship to this donor.")
    __properties: ClassVar[List[str]] = ["donor", "relationship_type"]

    @field_validator('relationship_type')
    def relationship_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['aunt', 'child', 'first cousin once removed', 'first cousin', 'fraternal twin', 'grandparent', 'half-sibling', 'niece', 'nephew', 'parent', 'paternal twin', 'sibling', 'second cousin', 'uncle']):
            raise ValueError("must be one of enum values ('aunt', 'child', 'first cousin once removed', 'first cousin', 'fraternal twin', 'grandparent', 'half-sibling', 'niece', 'nephew', 'parent', 'paternal twin', 'sibling', 'second cousin', 'uncle')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of RelatedDonor from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RelatedDonor from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "donor": obj.get("donor"),
            "relationship_type": obj.get("relationship_type")
        })
        return _obj


