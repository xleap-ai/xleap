# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional

from pydantic import BaseModel, Field, StrictStr
from typing_extensions import Annotated

from xleap._client.models.project_create_config import ProjectCreateConfig

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ProjectCreate(BaseModel):
    """
    ProjectCreate
    """  # noqa: E501

    id: Optional[StrictStr] = None
    config: Optional[ProjectCreateConfig] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    name: Annotated[str, Field(strict=True, max_length=100)]
    org: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = [
        "id",
        "config",
        "created_at",
        "updated_at",
        "name",
        "org",
    ]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ProjectCreate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "id",
                "created_at",
                "updated_at",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of config
        if self.config:
            _dict["config"] = self.config.to_dict()
        # set to None if org (nullable) is None
        # and model_fields_set contains the field
        if self.org is None and "org" in self.model_fields_set:
            _dict["org"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ProjectCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "config": ProjectCreateConfig.from_dict(obj.get("config"))
                if obj.get("config") is not None
                else None,
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
                "name": obj.get("name"),
                "org": obj.get("org"),
            }
        )
        return _obj
