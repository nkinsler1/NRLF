from typing import Annotated, List, Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator


class ParentCoding(BaseModel):
    model_config = ConfigDict(regex_engine="python-re", extra="forbid")
    id: Annotated[
        Optional[str],
        Field(
            description="Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.",
            pattern="[A-Za-z0-9\\-\\.]{1,64}",
        ),
    ] = None
    system: Annotated[
        Optional[str],
        Field(
            description="The identification of the code system that defines the meaning of the symbol in the code.",
            pattern="\\S*",
        ),
    ] = None
    version: Annotated[
        Optional[str],
        Field(
            description="The version of the code system which was used when choosing this code. Note that a well&ndash;maintained code system does not need the version reported, because the meaning of codes is consistent across versions. However this cannot consistently be assured, and when the meaning is not guaranteed to be consistent, the version SHOULD be exchanged.",
            pattern="[ \\r\\n\\t\\S]+",
        ),
    ] = None
    code: Annotated[
        Optional[str],
        Field(
            description="A symbol in syntax defined by the system. The symbol may be a predefined code or an expression in a syntax defined by the coding system (e.g. post&ndash;coordination).",
            pattern="[^\\s]+(\\s[^\\s]+)*",
        ),
    ] = None
    display: Annotated[
        Optional[str],
        Field(
            description="A representation of the meaning of the code in the system, following the rules of the system.",
            pattern="[ \\r\\n\\t\\S]+",
        ),
    ] = None
    userSelected: Annotated[
        Optional[bool],
        Field(
            description="Indicates that this coding was chosen by a user directly &ndash; e.g. off a pick list of available items (codes or displays)."
        ),
    ] = None


class ParentCodeableConcept(BaseModel):
    model_config = ConfigDict(regex_engine="python-re", extra="forbid")
    id: Annotated[
        Optional[str],
        Field(
            description="Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.",
            pattern="[A-Za-z0-9\\-\\.]{1,64}",
        ),
    ] = None
    coding: Optional[List[ParentCoding]] = None
    text: Annotated[
        Optional[str],
        Field(
            description="A human language representation of the concept as seen/selected/uttered by the user who entered the data and/or which represents the intended meaning of the user.",
            pattern="[ \\r\\n\\t\\S]+",
        ),
    ] = None


class ParentExtension(BaseModel):
    valueCodeableConcept: Annotated[
        Optional[ParentCodeableConcept],
        Field(
            description="A name which details the functional use for this link &ndash; see [http://www.iana.org/assignments/link&ndash;relations/link&ndash;relations.xhtml#link&ndash;relations&ndash;1](http://www.iana.org/assignments/link&ndash;relations/link&ndash;relations.xhtml#link&ndash;relations&ndash;1)."
        ),
    ] = None
    url: Annotated[
        Optional[str],
        Field(description="The reference details for the link.", pattern="\\S*"),
    ] = None


class Parent(BaseModel):
    @model_validator(mode="before")
    @classmethod
    def validate_empty_fields(cls, values):
        """
        Iteratively check every field in the model for emptiness.
        If a field is empty, add it to the error list with its full location.
        """
        allowed_classes = [
            "DocumentReference",
            "Narrative",
            "Identifier",
            "NRLCodeableConcept",
            "NRLCoding",
            "Reference",
            "DocumentReferenceRelatesTo",
            "CodeableConcept",
            "Coding",
            "DocumentReferenceContent",
            "Attachment",
            "NRLFormatCode",
            "ContentStabilityExtension",
            "ContentStabilityExtensionValueCodeableConcept",
            "ContentStabilityExtensionCoding",
            "DocumentReferenceContext",
            "Period",
        ]
        if cls.__name__ not in allowed_classes or not values:
            return values

        stack = [(None, values)]
        empty_fields = []

        while stack:
            path, current_value = stack.pop()

            if isinstance(current_value, dict):
                for key, value in current_value.items():
                    full_path = f"{path}.{key}" if path else key
                    if (
                        value is None
                        or value == ""
                        or (isinstance(value, list) and not value)
                    ):
                        empty_fields.append(full_path)
                    else:
                        stack.append((full_path, value))
                if not current_value:
                    empty_fields.append(path)

            elif isinstance(current_value, list):
                for index, item in enumerate(current_value):
                    full_path = f"{path}[{index}]" if path else f"[{index}]"
                    if (
                        item is None
                        or item == ""
                        or (isinstance(item, dict) and not item)
                    ):
                        empty_fields.append(full_path)
                    else:
                        stack.append((full_path, item))

            elif isinstance(current_value, Parent):
                nested_values = current_value.model_dump(exclude_none=True)
                for nested_field, nested_value in nested_values.items():
                    full_path = f"{path}.{nested_field}" if path else nested_field
                    stack.append((full_path, nested_value))

            else:
                if current_value is None or current_value == "":
                    empty_fields.append(path)

        if empty_fields:
            raise ValueError(
                f"The following fields are empty: {', '.join(empty_fields)}"
            )

        return values

    model_config = ConfigDict(regex_engine="python-re", extra="forbid")
    extension: Annotated[
        Optional[List[ParentExtension]],
        Field(description="A list of relevant extensions"),
    ] = None
