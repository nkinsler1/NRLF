from typing import Annotated, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from nrlf.consumer.fhir.r4.model import CodeableConcept


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
