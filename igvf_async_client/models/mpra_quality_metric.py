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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from igvf_async_client.models.attachment import Attachment
from typing import Optional, Set
from typing_extensions import Self

class MpraQualityMetric(BaseModel):
    """
    Schema for submission of a MPRA uniform pipeline quality metric.
    """ # noqa: E501
    preview_timestamp: Optional[StrictStr] = Field(default=None, description="The date the object was previewed.")
    status: Optional[StrictStr] = Field(default=None, description="The status of the metadata object.")
    release_timestamp: Optional[StrictStr] = Field(default=None, description="The date the object was released.")
    attachment: Optional[Attachment] = None
    lab: Optional[StrictStr] = Field(default=None, description="Lab associated with the submission.")
    award: Optional[StrictStr] = Field(default=None, description="Grant associated with the submission.")
    schema_version: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The version of the JSON schema that the server uses to validate the object.")
    uuid: Optional[StrictStr] = Field(default=None, description="The unique identifier associated with every object.")
    notes: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="DACC internal notes.")
    aliases: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="Lab specific identifiers to reference an object.")
    creation_timestamp: Optional[StrictStr] = Field(default=None, description="The date the object was created.")
    submitted_by: Optional[StrictStr] = Field(default=None, description="The user who submitted the object.")
    submitter_comment: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Additional information specified by the submitter to be displayed as a comment on the portal.")
    description: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="A plain text description of the object.")
    quality_metric_of: Optional[List[StrictStr]] = Field(default=None, description="The file(s) to which this quality metric applies.")
    analysis_step_version: Optional[StrictStr] = Field(default=None, description="The analysis step version of the quality metric.")
    pearson_correlation: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The correlation of log2 RNA/DNA ratios across tested sequences as a measure of replicable activity signal. Value is the median of replicate comparisons using only oligos with >= 10 barcodes.")
    median_barcodes_passing_filtering: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Median number of barcodes across tested sequences that passed filtering to determine if there was sufficient barcode to oligo coverage. Value is the median of all replicates.")
    median_rna_read_count: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Median of RNA read count for oligos that passed filtering to determine sufficient coverage in terms of read count. Value is the median of all replicates.")
    fraction_oligos_passing: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Fraction of tested sequences that passed filtering of the mappable sequences to determine if the designed library was sufficiently recovered. Value is the median of all replicates.")
    median_assigned_barcodes: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Median number of barcodes assigned to tested sequences in mapping as a quality control measure for the assignment step, whether there is sufficient barcode to oligo coverage.")
    fraction_assigned_oligos: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Fraction of assigned tested sequences in mapping to determine if the library during the assignment step was sufficiently recovered.")
    id: Optional[StrictStr] = Field(default=None, alias="@id")
    type: Optional[List[StrictStr]] = Field(default=None, alias="@type")
    summary: Optional[StrictStr] = Field(default=None, description="A summary of the quality metric.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["preview_timestamp", "status", "release_timestamp", "attachment", "lab", "award", "schema_version", "uuid", "notes", "aliases", "creation_timestamp", "submitted_by", "submitter_comment", "description", "quality_metric_of", "analysis_step_version", "pearson_correlation", "median_barcodes_passing_filtering", "median_rna_read_count", "fraction_oligos_passing", "median_assigned_barcodes", "fraction_assigned_oligos", "@id", "@type", "summary"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['archived', 'deleted', 'in progress', 'preview', 'released']):
            raise ValueError("must be one of enum values ('archived', 'deleted', 'in progress', 'preview', 'released')")
        return value

    @field_validator('schema_version')
    def schema_version_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\d+(\.\d+)*$", value):
            raise ValueError(r"must validate the regular expression /^\d+(\.\d+)*$/")
        return value

    @field_validator('notes')
    def notes_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(\S+(\s|\S)*\S+|\S)$", value):
            raise ValueError(r"must validate the regular expression /^(\S+(\s|\S)*\S+|\S)$/")
        return value

    @field_validator('submitter_comment')
    def submitter_comment_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(\S+(\s|\S)*\S+|\S)$", value):
            raise ValueError(r"must validate the regular expression /^(\S+(\s|\S)*\S+|\S)$/")
        return value

    @field_validator('description')
    def description_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(\S+(\s|\S)*\S+|\S)$", value):
            raise ValueError(r"must validate the regular expression /^(\S+(\s|\S)*\S+|\S)$/")
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
        """Create an instance of MpraQualityMetric from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of attachment
        if self.attachment:
            _dict['attachment'] = self.attachment.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MpraQualityMetric from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "preview_timestamp": obj.get("preview_timestamp"),
            "status": obj.get("status"),
            "release_timestamp": obj.get("release_timestamp"),
            "attachment": Attachment.from_dict(obj["attachment"]) if obj.get("attachment") is not None else None,
            "lab": obj.get("lab"),
            "award": obj.get("award"),
            "schema_version": obj.get("schema_version"),
            "uuid": obj.get("uuid"),
            "notes": obj.get("notes"),
            "aliases": obj.get("aliases"),
            "creation_timestamp": obj.get("creation_timestamp"),
            "submitted_by": obj.get("submitted_by"),
            "submitter_comment": obj.get("submitter_comment"),
            "description": obj.get("description"),
            "quality_metric_of": obj.get("quality_metric_of"),
            "analysis_step_version": obj.get("analysis_step_version"),
            "pearson_correlation": obj.get("pearson_correlation"),
            "median_barcodes_passing_filtering": obj.get("median_barcodes_passing_filtering"),
            "median_rna_read_count": obj.get("median_rna_read_count"),
            "fraction_oligos_passing": obj.get("fraction_oligos_passing"),
            "median_assigned_barcodes": obj.get("median_assigned_barcodes"),
            "fraction_assigned_oligos": obj.get("fraction_assigned_oligos"),
            "@id": obj.get("@id"),
            "@type": obj.get("@type"),
            "summary": obj.get("summary")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


