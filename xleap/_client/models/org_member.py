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
from typing import Any, ClassVar, Dict, List, Optional

from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing_extensions import Annotated

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class OrgMember(BaseModel):
    """
    OrgMember
    """  # noqa: E501

    id: Optional[StrictInt] = None
    username: StrictStr
    first_name: Optional[Annotated[str, Field(strict=True, max_length=150)]] = None
    last_name: Optional[Annotated[str, Field(strict=True, max_length=150)]] = None
    email: Optional[Annotated[str, Field(strict=True, max_length=254)]] = None
    __properties: ClassVar[List[str]] = [
        "id",
        "username",
        "first_name",
        "last_name",
        "email",
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
        """Create an instance of OrgMember from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "id",
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OrgMember from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "username": obj.get("username"),
                "first_name": obj.get("first_name"),
                "last_name": obj.get("last_name"),
                "email": obj.get("email"),
            }
        )
        return _obj
