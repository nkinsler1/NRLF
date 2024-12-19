from pydantic import BaseModel, ConfigDict


class Parent(BaseModel):
    model_config = ConfigDict(regex_engine="python-re", extra="forbid")
