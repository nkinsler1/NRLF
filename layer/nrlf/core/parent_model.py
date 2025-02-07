from typing import Annotated, List, Optional

from pydantic import BaseModel, ConfigDict, Field


class Coding(BaseModel):
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


class CodeableConcept(BaseModel):
    model_config = ConfigDict(regex_engine="python-re", extra="forbid")
    id: Annotated[
        Optional[str],
        Field(
            description="Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.",
            pattern="[A-Za-z0-9\\-\\.]{1,64}",
        ),
    ] = None
    coding: Optional[List[Coding]] = None
    text: Annotated[
        Optional[str],
        Field(
            description="A human language representation of the concept as seen/selected/uttered by the user who entered the data and/or which represents the intended meaning of the user.",
            pattern="[ \\r\\n\\t\\S]+",
        ),
    ] = None


class Extension(BaseModel):
    model_config = ConfigDict(regex_engine="python-re", extra="forbid")
    valueCodeableConcept: Annotated[
        Optional[CodeableConcept],
        Field(
            description="A name which details the functional use for this link &ndash; see [http://www.iana.org/assignments/link&ndash;relations/link&ndash;relations.xhtml#link&ndash;relations&ndash;1](http://www.iana.org/assignments/link&ndash;relations/link&ndash;relations.xhtml#link&ndash;relations&ndash;1)."
        ),
    ] = None
    url: Annotated[
        Optional[str],
        Field(description="The reference details for the link.", pattern="\\S*"),
    ] = None


class Parent(BaseModel):
    model_config = ConfigDict(regex_engine="python-re", extra="forbid")
    extension: Annotated[
        Optional[List[Extension]], Field(description="A list of relevant extensions")
    ]
